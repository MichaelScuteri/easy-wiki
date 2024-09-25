## Code block test

#### Python

```python
def helloworld():
    greeting = "arriving"
    if greeting == "arriving":
        print("Hey there")
    else:
        print("goodbye")
```

Dang, thats some nice code.

#### PowerShell

```PowerShell
function find-file($name) {
    ls -recurse -filter "*${name}*" -ErrorAction SilentlyContinue | 
    foreach {
        $place_path = $_.directory
        echo "${place_path}\${_}"
    }
}
```