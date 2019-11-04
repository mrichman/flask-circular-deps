# flask-circular-deps

This application has deliberate circular dependencies between model classes `ClassA` and `ClassB`.

Running this application will produce `ImportError: cannot import name 'ClassA' from 'myapp.models.classa'`.

