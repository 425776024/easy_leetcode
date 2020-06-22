function outf(text) {
    var mypre = document.getElementById("output");
    mypre.innerHTML = mypre.innerHTML + text;
}

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function runit(value) {
   var mypre = document.getElementById("output");
   mypre.innerHTML = '';
   Sk.pre = "output";
   Sk.configure({output:outf, read:builtinRead,__future__: Sk.python3});

   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
   var myPromise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("<stdin>", false, value, true);
   });
   myPromise.then(function(mod) {
       console.log('success');
   },
       function(err) {
//       console.log(err.toString());
       mypre.innerHTML=err.toString();
   });
}