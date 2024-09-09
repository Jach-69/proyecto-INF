module.exports = {
    parser: '@babel/eslint-parser',
    parserOptions: {
      requireConfigFile: false,
      ecmaVersion: 2020,
      sourceType: 'module',
    },
    extends: [
      'plugin:vue/essential',
      'eslint:recommended',
    ],
    rules: {
      'vue/multi-word-component-names': 'off',
    },
  }
  