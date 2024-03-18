from flask import Flask, render_template, request
from openai import OpenAI
from getpass import getpass
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import io
import base64
import re


input_file_1 = '''
{
"@context": "http://www.w3.org/ns/odrl.jsonld",
"@type": "Agreement",
"uid": "http://example.com/policy:101",
"profile": "http://example.com/odrl:profile:01",
"permission": [{
    "target": "http://example.com/creditApplication:001",
    "assigner": "http://example.com/creditApplicationOrg:002",
    "assignee": "http://example.com/customers:002",	
    "action": [{
        "rdf:value": {"@id": "odrl:creation"}, 
        "refinement": [{
            "leftOperand": "dateTime",
            "operator": "eq",
            "rightOperand": "https://www.wikidata.org/wiki/Q7722",
            "comment": "morning"}]}]
  }]
}
'''
input_file_2 = '''
{
"@context": "http://www.w3.org/ns/odrl.jsonld",
"@type": "Request",
"uid": "http://example.com/policy:102",
"profile": "http://example.com/odrl:profile:01",
"obligation": [{
    "target": "http://example.com/creditApplication:001",
    "assigner": "http://example.com/creditApplicationOrg:002",
    "assignee": "http://example.com/creditApplication:001",
    "action": [{
        "rdf:value": {"@id": "odrl:submission"},
        "includedIn":"creation"}]}]
}
'''
output_1e2 = '''
{
"uid": "http://example.org/BU1",
"res": ["credit-application", "physical"],
"ext-op": [{
    "name":"creation",
    "pre": ["time= https://www.wikidata.org/wiki/Q7722", "and", "person=customers:002"],   
    "rel": [{
        "type": "precedes",
        "op": [{
            "name":"submission", 
            "pre": ["person= creditApplication:001"]
        }]
    }]
	}]
}
'''
input_file_3 = '''
{
"@context": "http://www.w3.org/ns/odrl.jsonld",
"@type": "Assertion",
"uid": "http://example.com/policy:66",
"profile": "http://example.com/odrl:profile:01",
"permission": [{
    "target": "http://example.com/customerFile:001",
    "assigner": "http://example.com/orgCustomer:002",
    "action": [{
        "rdf:value": {"@id": "odrl:acceptance"},
        "refinement": [{
            "leftOperand": "dateTime",
            "operator": "gteq",
            "rightOperand": {"@value": "T9:00Z", "@type": "xsd:duration"}},
            {"leftOperand": "dateTime",
            "operator": "Iteq",
            "rightOperand": {"@value":"T12:00Z", "@type":"xsd:duration"}
            }],
        "includedIn":[{
            "rdf:value": {"@id":"odrl:verification"},
    		"refinement": [{
                "leftOperand": "payAmount",
                "operator": "eq",
                "rightOperand": "ZZ"}]
                }]
        }],
    "constraint": [{
        "leftOperand": "spatial",
        "operator": "eq",
        "rightOperand": "XX"
        }]
    }]
}
'''
output_3 = '''
{
"uid": "http://example.org/BU2",
"res": ["customer-file", "physical"],
"ext-op": [{
    "name":"verification",
    "pre":["location=XX","and", "budget=ZZ"],
    "rel": [{
        "type": "precedes",
        "op": [{
            "name":"acceptance",
            "pre": ["time>=T9:00Z", "and", "time<=T12:00Z"]}]
        }]
    }]
}
'''
input_file_6 = '''
{
"@context": "http://www.w3.org/ns/odrl.jsonld",
"@type": "Agreememt",
"uid": "http://example.com/policy:106",
"profile": "http://example.com/odrl:profile:01",
"permission": [{
    "target": "http://example.com/creditApplication:001",
    "assigner": 
    "http://example.com/creditApplicationOrg:002/manager",
    "assignee":"http://example.com/Customer:001",	
    "action": "due"
    }]
}
'''
output_6 = '''
{
"uid": "http://example.org/BU25",
"res": ["http://example.com/creditApplication:001", "physical"],
"ext-op": [{
    "name":"due",
	"pre": ["person=http://example.com/Customer:001"]
    }]
}
'''
input_file_12 = '''
{
"@context": "http://www.w3.org/ns/odrl.jsonld",
"@type": "Request",
"uid": "http://example.com/policy:003",
"profile": "http://example.com/odrl:profile:03",
"Obligation": [{
    "target": "http://example.com/customerFile:001",
    "assigner": "http://example.com/orgCustomer:002",
	"assignee": "http://example.com/Organization/clerk:001",
    "action": [{
        "rdf:value": {"@id": "odrl:opening"},
        "includedIn":[{
            "rdf:value": {"@id":"odrl:creation"}
        }]
    }]
	}]
}
'''
input_file_16 = '''
{
"@context": "http://www.w3.org/ns/odrl.jsonld",
"@type": "Agreement",
"uid": "http://example.com/policy:008",
"profile": "http://example.com/odrl:profile:01",
"Obligation": [{
    "target": "http://example.com/customerFile:001",
    "assigner": "http://example.com/orgCustomer:002",
    "assignee": "http://example.com/Organization/clerk:001",  
    "action": [{
        "rdf:value": {"@id": "odrl:creation"}, 
        "refinement": [{
            "leftOperand": "delayPeriod",
            "operator": "Iteq",
            "rightOperand": {"@value": "1PD", "@type": "xsd:duration"}}]
		}]
	}]
}
'''
output_12e16 = '''
{
"uid": "http://example.org/BU11",
"res": ["customer-file", "physical"],
"ext-op": [{
    "name":"creation",
    "pre": ["frequency<=1PD","and", "person=http://example.com/Organization/clerk:001"],
    "rel": [{
        "type": "precedes",
        "op": [{
            "name":"opening", 
            "pre": ["person=http://example.com/Organization/clerk:001"]
			}]
        }]
    }]
}
'''

app = Flask(__name__)

class ODRLApp:
    def __init__(self):
        self.openai_api_key = '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'
        self.client = OpenAI(api_key=self.openai_api_key)

        self.training_examples = [
            {
                "input": input_file_1,
                "output": output_1e2
            },
            {
                "input": input_file_2,
                "output": output_1e2
            },
            {
                "input": input_file_3,
                "output": output_3
            },
            {
                "input": input_file_6,
                "output": output_6
            },
             {
                "input": input_file_12,
                "output": output_12e16
            },
              {
                "input": input_file_16,
                "output": output_12e16
            },
        ]

    def extract_business_units(self, input_text):
        conversation = [
            {"role": "system", "content": "You are an expert in extract Business Units from a given ODRL specification."}
        ]
        for example in self.training_examples:
            conversation.append({"role": "user", "content": "file01: " + example["input"]})
            conversation.append({"role": "assistant", "content": example["output"]})
            print('pássou')

        conversation.append({"role": "user", "content": "file01: " + input_text})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=conversation
        )
        
        output_text = completion.choices[0].message.content
        return output_text
    


    
odrl_app = ODRLApp()

@app.route("/odrl", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form["input_text"]
        output_text = odrl_app.extract_business_units(input_text)
        return render_template("index.html", input_text=input_text, output_text=output_text)
    else:
        return render_template("index.html", input_text="", output_text="")




input_file_1_lifecycle = '''
{
  "uid": "http://example.org/BU1",
  "res": ["customer-file", "physical"],
  "ext-op": [{
    "name": "verification",
    "pre": "cond": [{"location": "XX", "and", "budget": "ZZ"}],
    "rel": [{
      "type": "precedes",
      "op": [{
        "name": "acceptance",
        "pre": "cond": [{"time >=": "T9:00Z", "and", "time <=": "T12:00Z"}]
      }]
    }]
  }]
}
'''

output_file_1_lifecycle = '''
Id Transition Type BU BU’s lifecycle
op0 creation external BUR1,1 created → opened
op1 opening internal
op2 verification external BUR1,2 verified → rejected | accepted
op21r
rejection internal
op22r archive external BUR1,3 archived → closed
op21a acceptance internal
op22a update external BUR1,4 updated
op23a archive external BUR1,3 archived → closed
op3 closure internal
op4 end internal
'''



class LifecycleApp:
    def __init__(self):
        self.openai_api_key = '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'
        self.client = OpenAI(api_key=self.openai_api_key)

        self.training_lifecycle = [
            {
                "input": input_file_1_lifecycle,
                "output": output_file_1_lifecycle
            },
        ]

    def extract_lifecycle(self, input_text):
        conversation = [
            {"role": "system", "content": "You are an expert in generating life cycles according to the given business unit."}
        ]
        for example in self.training_lifecycle:
            conversation.append({"role": "user", "content": "file01: " + example["input"]})
            conversation.append({"role": "assistant", "content": example["output"]})

        conversation.append({"role": "user", "content": "file01: " + input_text})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=conversation
        )
        
        output_text = completion.choices[0].message.content
        return output_text
    
lifecycle_app = LifecycleApp()

@app.route("/lifecycle", methods=["GET", "POST"])
def lifecycle():
    if request.method == "POST":
        input_text = request.form["input_text"]
        output_text = lifecycle_app.extract_lifecycle(input_text)
        return render_template("lifecycle.html", input_text=input_text, output_text=output_text)
    else:
        return render_template("lifecycle.html", input_text="", output_text="")

input_graph_1 = '''Id Transition Type BU BU’s lifecycle
op0 creation external BUR1,1 created → opened
op1 opening internal
op2 verification external BUR1,2 verified → rejected | accepted
op21r rejection internal
op22r archive external BUR1,3 archived → closed
op21a acceptance internal
op22a update external BUR1,4 updated
op23a archive external BUR1,3 archived → closed
op3 closure internal
op4 end internal'''

output_graph_1 = ''' graph TD;
    op0(creation) -->|external| op1(BUR1,1 created) -->|submitted| op2(submission);
    op2 -->|internal| op21a(acceptance) -->|external| op3(BUR1,2 approved) -->|rejected| op22r(closed);
    op21a -->|external| op22a(BUR1,4 updated);
    op3 -->|internal| op4(closure) -->|internal| op23a(BUR1,3 archived) -->|closed| op5(end);
'''

class MermaidCodeApp:
    def __init__(self):
        self.openai_api_key = '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'
        self.client = OpenAI(api_key=self.openai_api_key)
        
        self.training_graph = [
            {
                "input": input_graph_1,
                "output": output_graph_1
            },
        ]

    def extract_mermaid(self, input_text):
        conversation = [
            {"role": "system", "content": "Put this in a schema that mermaid accepts > graph TD "}
        ]
        
        for example in self.training_graph:
            conversation.append({"role": "user", "content": "file01: " + example["input"]})
            conversation.append({"role": "assistant", "content": example["output"]})

        conversation.append({"role": "user", "content": "file01: " + input_text})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=conversation
        )
        
        formatted_output = completion.choices[0].message.content
        output_text = re.sub(r'```mermaid|```', '', formatted_output)
        return output_text


mermaidCode_app = MermaidCodeApp()

@app.route("/graph", methods=["GET", "POST"])
def mermaid():
    if request.method == "POST":
        input_text = request.form["input_text"]
        output_text = mermaidCode_app.extract_mermaid(input_text)
        return render_template("graph.html", input_text=input_text, output_text=output_text)
    else:
        return render_template("graph.html", input_text="", output_text="")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
