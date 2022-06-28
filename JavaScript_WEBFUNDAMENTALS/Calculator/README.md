### 4 Function Calculator
Using what we've learned about:

* variables
* conditionals
* onclick

And the following code snippets:

* var displayDiv = document.querySelector("#display");
* displayDiv.innerText = "Some new value";

Try to build a 4 Function Calculator from scratch.

We'll provide some HTML to get you started, and check out a working demo embedded below!

**Starter HTML**
```
<div id="calculator">
  <div id="display">0</div>
  <div class="row">
    <button onclick="press(7);">7</button>
    <button onclick="press(8);">8</button>
    <button onclick="press(9);">9</button>
    <button class="operator" onclick="setOP('/');">÷</button>
  </div>
  <div class="row">
    <button onclick="press(4);">4</button>
    <button onclick="press(5);">5</button>
    <button onclick="press(6);">6</button>
    <button class="operator" onclick="setOP('*');">×</button>
  </div>
  <div class="row">
    <button onclick="press(1);">1</button>
    <button onclick="press(2);">2</button>
    <button onclick="press(3);">3</button>
    <button class="operator" onclick="setOP('-');">−</button>
  </div>
  <div class="row">
    <button onclick="clr();">C</button>
    <button onclick="press(0);">0</button>
    <button onclick="press('.');">.</button>
    <button class="operator" onclick="setOP('+');">+</button>
  </div>
  <div class="row">
    <button id="equals" onclick="calculate()">=</div>
  </div>
<div>
```




