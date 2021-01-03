# Reactive cells cli
A cli tool to demonstrate reactive functionality similar to spreadsheet function and values.


### Installing

Clone the source code from github:

```
git clone git@github.com:Shlomo-T/c.git
```

Install it into virtual environment:

```
cd reactive-cells-cli
python3 -m venv ./venv
source ./venv/bin/activate
pip install --editable . 
```

The code works with local MongoDB as a persistent database
```
docker run -d --name mongodb mongo:4.0.4
```
### How to use

After installation check that the cli is really working, you should see short explanation about reactive-cells-cli and the available commands
```
reactive-cells-cli 
```

Initializing the cli data from file
```
reactive-cells-cli init <file-path>
```

Current state command aka "a"
```
reactive-cells-cli current-state
```

Modifying existing index aka "b"
```
reactive-cells-cli modify-value <index> <value or formula>
```

## Code Assumptions
* init command expect to receive a valid file with integers and formulas separated by commas.
  The order formulas is crucial and must relay on previous indexes only, otherwise an exception will be thrown.
* modify-value command will throw exception if not existing index will be provided.
* modify-value command will set or recalculate the index value and will update 1st depth dependent indexes only.
  I choose this approach to avoid circular dependencies issues that can cause an endless recursion if it's not handled
  appropriately.


## Authors

* **Shlomo Tadela** - *projects* - [Shlomo-T](https://github.com/Shlomo-T/)