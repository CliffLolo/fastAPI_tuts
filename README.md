# fastAPI_tuts

### Installing FastAPI
``` pip install fastapi```

### Installing an ASGI server
```pip install "uvicorn[standard]"``` 
### Run the seerver with:
```uvicorn main:app --reload```


```main```: the file main.py (the Python "module").

```app```: the object created inside of main.py with the line app = FastAPI().

`````--reload`````: make the server restart after code changes. Only do this for development.