module.exports = {

    "env": {
        "es6": true,
        "node": true,
        "commonjs": true,
        "amd": true,
        "browser": true,
    },
    "extends": [
        "eslint:recommended",
        "plugin:vue/essential"
    ],
    "globals": {
        "Atomics": "readonly",
        "SharedArrayBuffer": "readonly"
    },
    "parserOptions": {
        "ecmaVersion": 2018,
        "sourceType": "module"
    },
    "plugins": [
        "vue",
        
    ],
    "rules": {
      'no-console': 'off',
       "max-len" : ["error", {code : 300}] ,
       "linebreak-style": ["off","windows"],
       "no-undef": 0, // 可以 有未定义的变量
    }
},
{
	"presets": ["env"],
	"plugins": ["syntax-dynamic-import"]
};
