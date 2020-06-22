function mdSwitch() {
        var mdValue = document.getElementById("md_v").innerText;
        var converter = new showdown.Converter();
        var html = converter.makeHtml(mdValue);
        document.getElementById("show-area").innerHTML = html;
};

window.onload = function () {
    mdSwitch();
    var el = document.getElementById("editor");
	var version = "# version: Python3\n";
	var codeAreaTip = "# Edit your code here:\n \n";
	var code = "print('hello world')";
//    var initValue = version + codeAreaTip  + code;
    var myCodeMirror = CodeMirror.fromTextArea(el, {
        mode: "python",
        theme: "leetcode",
        keyMap: "sublime",
        lineNumbers: true,
        smartIndent: true,
        indentUnit: 4,
        indentWithTabs: false,
        lineWrapping: true,
        gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter", "CodeMirror-lint-markers"],
        foldGutter: true,
        autofocus: true,
        matchBrackets: true,
        autoCloseBrackets: true,
        styleActiveLine: true,
    });
//    myCodeMirror.setOption("value", initValue);
    myCodeMirror.on("keypress", function() {
        myCodeMirror.showHint(); // 注意，注释了CodeMirror库中show-hint.js第131行的代码（阻止了代码补全，同时提供智能提示）
    });
    var run_btn = document.getElementById("run_btn");
    var save_btn = document.getElementById("save_btn");
    var edit_md = document.getElementById("edit_md");
    edit_md.onclick = function() {
        var name_v = document.getElementById("code_name").innerText;
        host = window.location.host;
        url='http://'+host+'/md/'+name_v;
        window.open(url);
    };
    run_btn.onclick = function() {
        var value = myCodeMirror.getValue();
//        console.log(value);
//        alert(value);
        runit(value);

    };
    save_btn.onclick = function() {
        var value = myCodeMirror.getValue();
        var name_v = document.getElementById("code_name").innerText;
        axios.put('/save', {
                    "code_str":value,
                    "name":name_v,
                  })
                  .then(function (response) {
                  })
                  .catch(function (error) {
                    console.log(error);
                  });

    };
};