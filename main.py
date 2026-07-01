from fastapi import FastAPI,middleware
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
import os

app = FastAPI()

middleware(
    
)
class QueryRequest(BaseModel):
    query: str

@app.post('/query')
async def query_travel_agent(query:QueryRequest):

    try:
        print(query)
        graph = GraphBuilder(model_provider='groq')
        react_app = graph()
        #react_app = graph.build_graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("My_graph.png",'wb') as f:
            f.write(png_graph)


        print(f"Graph saved as 'My_graph.png' in {os.getcwd()}")


        #assuming request is a pydantic object like: {"question": "your text"}
        messages = {"messages": {query.question}}
        output = react_app.invoke(messages)


        #if the result is dict with messages:
        if isinstance(output,dict) and "messages" in output:
            final_output = output["messages"][-1].content  #last ai responce
        else:
            final_output = str(output)
        
        return {"Answer": final_output}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})