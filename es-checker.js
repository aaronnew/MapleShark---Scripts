// var title = document.title;

var window = {};
// var circleField = document.querySelector('#circle');
(function e(t, n, r) { function s(o, u) { if (!n[o]) { if (!t[o]) { var a = typeof require == "function" && require; if (!u && a) return a(o, !0); if (i) return i(o, !0); var f = new Error("Cannot find module '" + o + "'"); throw f.code = "MODULE_NOT_FOUND", f } var l = n[o] = { exports: {} }; t[o][0].call(l.exports, function (e) { var n = t[o][1][e]; return s(n ? n : e) }, l, l.exports, e, t, n, r) } return n[o].exports } var i = typeof require == "function" && require; for (var o = 0; o < r.length; o++)s(r[o]); return s })({
  1: [function (require, module, exports) {
    var api = {
      letConst: { passes: "'use strict'; let a; const b = 2;" },
      letLoop: { passes: "'use strict'; for(let i in {}){}; for(let i=0;;){break}" },
      constLoop: { passes: "'use strict'; for(const i in {}){}; for (const i=0;;){break}" },
      defaultParameter: { passes: "'use strict'; function a(b=2){}" },
      spreadRest: { passes: "'use strict'; var a = [1,2]; +function b(...c){}(...a);" },
      destructuring: { passes: "'use strict'; var a = [1,2], [b,c] = a, d = {e:1,f:2}, {e:E,f} = d;" },
      parameterDestructuring: { passes: "'use strict'; function a({b,c}){}" },
      templateString: { passes: "'use strict'; var a = 1, b = `c${a}d`;" },
      forOf: { passes: "'use strict'; for (var a of [1]) {}" },
      arrow: { passes: "'use strict'; var a = () => {};" },
      generator: { passes: "'use strict'; function *a(){ yield; }" },
      conciseMethodProperty: { passes: "'use strict'; var a = 1, b = { c(){}, a };" },
      computedProperty: { passes: "'use strict'; var a = 1, b = { ['x'+a]: 2 };" },
      moduleExport: { passes: "'use strict'; export var a = 1;" },
      moduleImport: { passes: "'use strict'; import {a} from 'b';" },
      classes: { passes: "'use strict'; class Foo {}; class Bar extends Foo {};" },
      numericLiteral: { passes: "'use strict'; var a = 0o1, b = 0b10;" },
      oldOctalLiteral: { passes: "var a = 01;" },
      symbol: { passes: "'use strict'; var a = Symbol('b');" },
      symbolImplicitCoercion: { dependencies: ["symbol"], fails: "'use strict'; var a = Symbol('a'); a + '';" },
      unicodeEscape: { passes: "'use strict'; var a = '\\u{20BB7}';" },
      unicodeIdentifier: { passes: "'use strict'; var \\u{20BB7};" },
      unicodeRegExp: { passes: "'use strict'; var a = /\\u{20BB7}/u;" },
      stickyRegExp: { passes: "'use strict'; var a = /b/y;" },
      letTDZ: { dependencies: ["letConst"], fails: "'use strict'; a = 1; let a;" },
      letLoopScope: { dependencies: ["letLoop", "forOf"], passes: "'use strict'; var x=[],i=0;for(let i=2;i<3;i++){x.push(function(){return i})};for(let i in {3:0}){x.push(function(){return i})};for(let i of [4]){x.push(function(){return i})};if(x[0]()*x[1]()*x[2]()!=24) throw 0;" },
      constRedef: { dependencies: ["letConst"], fails: "'use strict'; const a = 1; a = 2;" },
      objectProto: { passes: "'use strict'; var a = { b: 2 }, c = { __proto__: a }; if (c.b !== 2) throw 0;" },
      objectSuper: { passes: "'use strict'; var a = { b: 2 }, c = { d() { return super.b; } }; Object.setPrototypeOf(c,a); if (c.d() !== 2) throw 0;" },
      extendNatives: { dependencies: ["class"], passes: "'use strict'; class Foo extends Array { }; var a = new Foo(); a.push(1,2,3); if (a.length !== 3) throw 0;" },
      TCO: { passes: "'use strict'; +function a(b){ if (b<6E4) a(b+1); }(0);" },
      functionNameInference: { passes: "'use strict'; var a = { b: function(){} }; if (a.b.name != 'b') throw 0;" },
      ObjectStatics: { is: "'use strict'; return ('getOwnPropertySymbols' in Object) && ('assign' in Object) && ('is' in Object);" },
      ArrayStatics: { is: "'use strict'; return ('from' in Array) && ('of' in Array);" },
      ArrayMethods: { is: "'use strict'; return ('fill' in Array.prototype) && ('find' in Array.prototype) && ('findIndex' in Array.prototype) && ('entries' in Array.prototype) && ('keys' in Array.prototype) && ('values' in Array.prototype);" },
      TypedArrays: { is: "'use strict'; return ('ArrayBuffer' in global) && ('Int8Array' in global) && ('Uint8Array' in global) && ('Int32Array' in global) && ('Float64Array' in global);" },
      TypedArrayStatics: { dependencies: ["TypedArrays"], is: "'use strict'; return ('from' in Uint32Array) && ('of' in Uint32Array);" },
      TypedArrayMethods: { dependencies: ["TypedArrays"], is: "'use strict'; var x = new Int8Array(1); return ('slice' in x) && ('join' in x) && ('map' in x) && ('forEach' in x);" },
      StringMethods: { is: "'use strict'; return ('includes' in String.prototype) && ('repeat' in String.prototype);" },
      NumberStatics: { is: "'use strict'; return ('isNaN' in Number) && ('isInteger' in Number);" },
      MathStatics: { is: "'use strict'; return ('hypot' in Math) && ('acosh' in Math) && ('imul' in Math);" },
      collections: { is: "'use strict'; return ('Map' in global) && ('Set' in global) && ('WeakMap' in global) && ('WeakSet' in global);" },
      Proxy: { is: "'use strict'; return ('Proxy' in global);" },
      Promise: { is: "'use strict'; return ('Promise' in global);" },
      Reflect: { is: "'use strict'; return ('Reflect' in global);" },
    };

    module.exports = api;

  }, {}], 2: [function (require, module, exports) {
    var Supports = function () {
      // Variables
      this.letConst = 'letConst';
      this.letTDZ = 'letTDZ';
      this.constRedef = 'constRedef';
      this.destructuring = 'destructuring';
      this.spreadRest = 'spreadRest';
      // Data Types
      this.forOf = 'forOf';
      this.collections = 'collections';
      this.symbol = 'symbol';
      this.Symbol = this.symbol;
      this.symbolImplicitCoercion = 'symbolImplicitCoercion';
      // Number
      this.numericLiteral = 'numericLiteral';
      this.oldOctalLiteral = 'oldOctalLiteral';
      this.MathStatics = 'MathStatics';
      this.mathStatics = this.MathStatics;
      this.NumberStatics = 'NumberStatics';
      this.numberStatics = this.NumberStatics;
      // String
      this.StringMethods = 'StringMethods';
      this.stringMethods = this.StringMethods;
      this.unicodeEscape = 'unicodeEscape';
      this.unicodeIdentifier = 'unicodeIdentifier';
      this.unicodeRegExp = 'unicodeRegExp';
      this.stickyRegExp = 'stickyRegExp';
      this.templateString = 'templateString';
      // Function
      this.arrow = 'arrow';
      this.defaultParameter = 'defaultParameter';
      this.parameterDestructuring = 'parameterDestructuring';
      this.functionNameInference = 'functionNameInference';
      this.TCO = 'TCO';
      this.tco = this.TCO;
      // Array
      this.ArrayMethods = 'ArrayMethods';
      this.arrayMethods = this.ArrayMethods;
      this.ArrayStatics = 'ArrayStatics';
      this.arrayStatics = this.ArrayStatics;
      this.TypedArrayMethods = 'TypedArrayMethods';
      this.typedArrayMethods = this.TypedArrayMethods;
      this.TypedArrayStatics = 'TypedArrayStatics';
      this.typedArrayStatics = this.TypedArrayStatics;
      this.TypedArrays = 'TypedArrays';
      this.typedArrays = this.TypedArrays;
      // Object
      this.objectProto = 'objectProto';
      this.ObjectStatics = 'ObjectStatics';
      this.objectStatics = this.ObjectStatics;
      this.computedProperty = 'computedProperty';
      this.conciseMethodProperty = 'conciseMethodProperty';
      this.Proxy = 'Proxy';
      this.proxy = this.Proxy;
      this.Reflect = 'Reflect';
      this.reflect = this.Reflect;
      // Generator and Promise
      this.generator = 'generator';
      this.Promise = 'Promise';
      this.promise = this.Promise;
      // Class
      this.classes = 'classes';
      this.class = this.classes;
      this.objectSuper = 'objectSuper';
      this.extendNatives = 'extendNatives';
      // Module
      this.moduleExport = 'moduleExport';
      this.moduleImport = 'moduleImport';
    };

    module.exports = new Supports();

  }, {}], 3: [function (require, module, exports) {
    var api = require('./api');
    var supports = {};
    supports._api = api;

    function runTest(key) {
      if (key === 'class') key = 'classes';
      if (supports._api[key].dependencies) {
        for (var i = 0; i < supports._api[key].dependencies.length; i++) {
          var depKey = supports._api[key].dependencies[i];
          if (runTest(depKey) === false) return false;
        }
      }

      if (supports._api[key].passes) {
        return tryPassFail(supports._api[key].passes);
      } else if (supports._api[key].fails) {
        return !tryPassFail(supports._api[key].fails);
      } else if (supports._api[key].is) {
        return tryReturn(supports._api[key].is);
      } else if (supports._api[key].not) {
        return !tryReturn(supports._api[key].not);
      }
    }

    function tryPassFail(code) {
      try {
        runIt(code);
        return true;
      }
      catch (err) {
        return false;
      }
    }

    function tryReturn(code) {
      try {
        return runIt(code);
      }
      catch (err) {
        return false;
      }
    }

    function runIt(code) {
      return (new Function(code))();
    }

    module.exports = runTest;

  }, { "./api": 1 }], 4: [function (require, module, exports) {
    var supports = require('../../lib/interface');
    var api = require('../../lib/api');
    var runTest = require('../../lib/runtest');

    //  global = window;
    for (var key in supports) {
      supports[key] = runTest(supports[key]);
    }

    supports._api = api;
    window.Supports = supports;

  }, { "../../lib/api": 1, "../../lib/interface": 2, "../../lib/runtest": 3 }]
}, {}, [4]);


var mapper = {
  letConst: {
    cn: 'let 和 const 命令',
    en: 'let and const',
    example: 'let a;\nconst b = 2;'
  },
  defaultParameter: {
    cn: '函数的默认参数',
    en: 'default function parameter values',
    example: 'function a(b=2){}'
  },
  spreadRest: {
    cn: '扩展（...）运算符',
    en: '... operator',
    example: 'var a = [1,2];\nfunction b(...c){}(...a);'
  },
  destructuring: {
    cn: '解构赋值',
    en: 'destructuring assignments/declarations for arrays and objects',
    example: 'var a = [1,2];\nvar [b,c] = a;\nvar d = {e:1,f:2};\nvar {e:E,f} = d;'
  },
  parameterDestructuring: {
    cn: '函数参数的解构',
    en: 'destructuring for function parameters',
    example: 'function a({b,c}){};'
  },
  templateString: {
    cn: '模板字符串',
    en: 'Template String Literals',
    example: 'var a = 1;\nvar b = `c${a}d`;'
  },
  forOf: {
    cn: 'for...of循环',
    en: 'For...of loop',
    example: 'for (var v of something) { .. };'
  },
  arrow: {
    cn: '箭头函数',
    en: 'arrow function',
    example: 'x => x * x'
  },
  generator: {
    cn: 'Generator函数',
    en: 'Generator function',
    example: 'function *foo() { .. }'
  },
  conciseMethodProperty: {
    cn: '对象属性的简洁表示法',
    en: 'Object Literal Property Shorthands',
    example: 'var o = { b() { .. }, a };'
  },
  computedProperty: {
    cn: '对象属性名使用表达式',
    en: 'Object Literal Computed Property',
    example: 'o = { ["a" + "b"]: 42 }'
  },
  moduleExport: {
    cn: '模块的export命令',
    en: 'Module export command',
    example: 'export default foo = 42'
  },
  moduleImport: {
    cn: '模板的import命令',
    en: 'Module import command',
    example: 'import bar from "foo"'
  },
  numericLiteral: {
    cn: '数值的八进制（例如 0o1）和二进制（例如 0b10）表示法',
    en: 'Octal (e.g. 0o1 ) and binary (e.g. 0b10 ) literal forms',
    example: 'var x = 0o1;\nvar y = 0b10;'
  },
  oldOctalLiteral: {
    cn: '不再支持八进制的前缀零表示法（例如01）',
    en: 'Old octal literal invalid now (e.g. 01 )',
    example: 'var x = 01;'
  },
  symbol: {
    cn: 'Symbol类型',
    en: 'Symbol',
    example: 'var a = Symbol("b");'
  },
  unicodeEscape: {
    cn: 'Unicode字符的大括号表示法（例如 \\u{20BB7}）',
    en: 'Unicode code-point escape form in string literals (e.g. \\u{20BB7} )',
    example: 'var x = "\\u{20BB7}";'
  },
  unicodeIdentifier: {
    cn: 'Unicode字符是否可用作标识名（例如 \\u{20BB7} = 42;）',
    en: 'Unicode code-point escape form in identifier names (e.g. var \\u{20BB7} = 42; )',
    example: 'var \\u{20BB7} = 42;'
  },
  unicodeRegExp: {
    cn: '正则表达式的u修饰符（例如 var regexp = /\\u{20BB7}/u;）',
    en: 'Unicode code-point escape form in regular expressions (e.g. var regexp = /\\u{20BB7}/u; )',
    example: 'var regexp = /\\u{20BB7}/u;'
  },
  stickyRegExp: {
    cn: '正则表达式的y修饰符（例如 /b/y）',
    en: 'y flag for sticky regular expressions (e.g. /b/y )',
    example: 'var a = /b/y;'
  },
  classes: {
    cn: '类（class）',
    en: 'Class',
    example: 'class A extends B { .. }'
  },
  class: {
    cn: '类（class）',
    en: 'Class',
    example: 'class A extends B { .. }'
  },
  letTDZ: {
    cn: 'let命令的暂时性死区',
    en: 'TDZ error for too-early access of let or const declarations',
    example: 'if (1) {\n  typeof x; // ReferenceError\n  let x;\n}'
  },
  constRedef: {
    cn: '不允许再次用const声明同一变量',
    en: 'Redefinition of const declarations not allowed',
    example: 'const a = 1;\na = 2;'
  },
  objectProto: {
    cn: '对象的__proto__属性',
    en: '__proto__ in object literal definition sets [[Prototype]] link',
    example: 'var a = { b: 2 };\nvar c = { __proto__: a };\nf (c.b !== 2) throw 0;'
  },
  objectSuper: {
    cn: '对象方法是否可以使用super',
    en: 'super allowed in object methods',
    example: 'var a = { b: 2 };\nvar c = { d() { return super.b; } };\nvar Object.setPrototypeOf(c,a);\nif (c.d() !== 2) throw 0;'
  },
  extendNatives: {
    cn: '原生类型的扩展',
    en: 'class ABC extends Array { .. }',
    example: 'class Foo extends Array { };'
  },
  TCO: {
    cn: '尾调用优化',
    en: 'Tail-call optimization for function calls and recursion',
    example: 'function a(b){ if (b<2E20) a(b+1); }(0);'
  },
  symbolImplicitCoercion: {
    cn: 'Symbol值不能用于运算',
    en: 'Symbols cannot be implicitly coerced',
    example: 'var x = Symbol("a") + "";'
  },
  functionNameInference: {
    cn: '匿名函数的name属性推断函数名',
    en: 'Inferences for function name property for anonymous functions',
    example: 'var o = { \n  ["foo"](){},\n  [Symbol.for("foo")](){}\n}\n\nconsole.log( o.foo.name ); // "foo"\nconsole.log( o[Symbol.for("foo")].name ); // "[foo]"',
    url: ['https://github.com/babel/babel/issues/993']
  },
  ObjectStatics: {
    cn: 'Object的静态方法（Object.getOwnPropertySymbols(), Object.assign()）',
    en: 'Static functions added to Object (Object.getOwnPropertySymbols(), Object.assign() )',
    example: 'Object.getOwnPropertySymbols();\nObject.assign();'
  },
  ArrayStatics: {
    cn: '数组的静态方法（Array.from(), Array.of()）',
    en: 'Static functions added to Array (Array.from(), Array.of() )',
    example: 'Array.from();\nArray.of()'
  },
  ArrayMethods: {
    cn: '数组的实例方法（[].fill(), [].find(), [].findIndex(), [].entries(), [].keys(), [].values()）',
    en: 'Methods added to Array.prototype ([].fill(), [].find(), [].findIndex(), [].entries(), [].keys(), [].values() )',
    example: 'Array.prototype.fill();\nArray.prototype.find();\nArray.prototype.findIndex();\nArray.prototype.entries();\nArray.prototype.keys();Array.prototype.values();'
  },
  TypedArrays: {
    cn: '类型化数组（Uint8Array, ArrayBuffer, Int8Array(), Int32Array(), Float64Array()）',
    en: 'TypedArrays like Uint8Array, ArrayBuffer, Int8Array(), Int32Array(), Float64Array()',
    example: 'ArrayBuffer();\nInt8Array();\nUint8Array();\nInt32Array();\nFloat64Array();'
  },
  TypedArrayStatics: {
    cn: '类型化数组的静态方法（例如 Uint32Array.from(), Uint32Array.of()）',
    en: 'Some Array statics (e.g. Uint32Array.from(), Uint32Array.of() ) added to the TypedArray constructors',
    example: 'Uint32Array.from();\nUint32Array.of();'
  },
  TypedArrayMethods: {
    cn: '类型化数组的实例方法（例如 Int8Array.prototype.slice(), Int8Array.prototype.join(), Int8Array.prototype.forEach()）',
    en: 'Some Array methods (e.g. Int8Array.prototype.slice(), Int8Array.prototype.join(), Int8Array.prototype.forEach() ) added to the TypedArray prototypes',
    example: 'Int8Array.prototype.slice();\nInt8Array.prototype.join();\nInt8Array.prototype.map();\nInt8Array.prototype.forEach();'
  },
  StringMethods: {
    cn: '字符串的实例方法（String.prototype.includes(), String.prototype.repeat()）',
    en: 'Methods added to String.prototype (String.prototype.includes(), String.prototype.repeat() )',
    example: 'String.prototype.includes();\nString.prototype.repeat();'
  },
  NumberStatics: {
    cn: 'Number对象的静态方法（Number.isNaN(), Number.isInteger()）',
    en: 'Static functions added to Number (Number.isNaN(), Number.isInteger() )',
    example: 'Number.isNaN();\nNumber.isInteger();'
  },
  MathStatics: {
    cn: 'Math对象的静态方法（例如 Math.hypot(), Math.acosh(), Math.imul()）',
    en: 'Static functions added to Math (e.g. Math.hypot(), Math.acosh(), Math.imul() )',
    example: 'Math.hypot();\nMath.acosh();\nMath.imul();'
  },
  collections: {
    cn: 'Map, Set, WeakMap, WeakSet',
    en: 'Map, Set, WeakMap, WeakSet',
    example: 'new Map();\nnew Set();\nnew WeakMap();\nnew WeakSet();'
  },
  Proxy: {
    cn: 'Proxy对象',
    en: 'Proxies',
    example: 'new Proxy();'
  },
  Promise: {
    cn: 'Promise对象',
    en: 'Promises',
    example: 'new Promise();'
  },
  Reflect: {
    cn: 'Reflect对象',
    en: 'Reflect',
    example: 'Reflect.get(obj, "foo");'
  },
  everything: {
    cn: '所有特性',
    en: 'Everything',
    example: ''
  }
};

module.exports = mapper;
// circleField.innerHTML = '<div class="c100 p0 big orange">' +
//   '  <span>0%</span>' +
//   '<div class="slice">' +
//   '  <div class="bar"></div>' +
//   '  <div class="fill"></div>' +
//   '</div>' +
//   '</div>';

// var circleField = document.querySelector('#circle-title');
// circleField.innerHTML = '  <h2>您的浏览器支持<span></span>的 ECMAScript 6。</h2>';

// var header = document.querySelector('div[data-role="header"]');
// header.innerHTML = '      <a data-iconpos="notext" data-role="button" title="Home"></a>' +
//   '    <h1>ES-Checker <small>(<a style="color:orange;" href="https://github.com/ruanyf/es-checker">Github</a>)</small></h1>' +
//   '    <a href="#" onclick="document.location=\'http://ruanyf.github.io/es-checker/index.html\';">英文 | 中文</a>';

// var footer = document.querySelector('div[data-role="footer"]');
// footer.innerHTML = '<h4><a style="color:orange;" href="https://github.com/ruanyf/es-checker">ES-Checker</a> by <a style="color:orange;" href="https://github.com/ruanyf">ruanyf</a> @2015</h4>';

var pass = 0;
var total = 0;

runSuite('Variables', ['letConst', 'letTDZ', 'constRedef', 'destructuring', 'spreadRest']);

runSuite('Data Types', ['forOf', 'collections', 'symbol', 'symbolImplicitCoercion']);

runSuite('Number', ['numericLiteral', 'oldOctalLiteral', 'mathStatics', 'numberStatics']);

runSuite('String', ['stringMethods', 'unicodeEscape', 'unicodeIdentifier', 'unicodeRegExp', 'stickyRegExp', 'templateString']);

runSuite('Function', ['arrow', 'defaultParameter', 'parameterDestructuring', 'functionNameInference', 'tco']);

runSuite('Array', ['arrayMethods', 'arrayStatics', 'typedArrays', 'typedArrayMethods', 'typedArrayStatics']);

runSuite('Object', ['objectProto', 'objectStatics', 'computedProperty', 'conciseMethodProperty', 'proxy', 'reflect']);

runSuite('Generator and Promise', ['generator', 'promise']);

runSuite('Class', ['class', 'objectSuper', 'extendNatives']);

runSuite('Module', ['moduleExport', 'moduleImport']);

function runSuite(title, testArray) {
  // var divSet = document.querySelector('div[data-role="collapsible-set"]');
  // var div = document.createElement("div");
  // div.setAttribute("data-role", "collapsible");
  // div.setAttribute("data-collapsed-icon", "flat-eye");
  // div.setAttribute("data-expanded-icon", "flat-eye");
  // if (total === 0) div.setAttribute("data-collapsed", "false");
  // div.innerHTML = '<h3>' + title + '</h3>';
  console.log(title);
  testArray.forEach(function (key) {
    if (window.Supports[key]) {
      pass += 1;
      console.log('' + ' ✓ ' + getApi(key).cn + '');
    } else {
      console.log('' + ' ✖ ' + getApi(key).cn + '');
    }
    //total += 1;
  });
  // divSet.appendChild(div);
}

function getApi(key) {
  if (mapper[key]) {
    return mapper[key];
  } else if (mapper[key[0].toUpperCase() + key.substring(1)]) {
    return mapper[key[0].toUpperCase() + key.substring(1)];
  } else if (mapper[key.toUpperCase()]) {
    return mapper[key.toUpperCase()];
  }
}


// var rate = parseInt((pass / total) * 100);
// var circle = document.querySelector('.c100');
// circle.classList.remove('p0');
// circle.classList.add('p' + rate);
// var circleSpan = document.querySelector('.c100 span');
// circleSpan.innerHTML = rate + '%';
// var h2Span = document.querySelector('fieldset h2 span');
// h2Span.innerHTML = rate + '%';

// setTimeout(function () { document.title = title; }, 0);
