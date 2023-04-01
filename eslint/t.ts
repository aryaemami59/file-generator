type Severity = 0 | 1 | 2;
type StringSeverity = "off" | "warn" | "error";
type RuleLevel = Severity | StringSeverity;
type RuleEntry = RuleLevel | [RuleLevel, any];
type RulesRecord = {
  [rule: string]: RuleEntry;
};
interface HasRules<Rules extends RulesRecord = RulesRecord> {
  rules?: Rules | undefined;
}
type ECMAVERSION = 3 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | "latest";
type SOURCETYPE = "script" | "module";
type ECMAFEATURES = {
  globalReturn?: boolean | undefined;
  impliedStrict?: boolean | undefined;
  jsx?: boolean | undefined;
  experimentalObjectRestSpread?: boolean | undefined;
  [key: string]: any;
};
type ParserOptions = {
  ecmaVersion?: ECMAVERSION | undefined;
  sourceType?: SOURCETYPE | undefined;
  ecmaFeatures?: ECMAFEATURES | undefined;
  [key: string]: any;
};
type ENV = {
  [name: string]: boolean;
};
type G = "off" | "readonly" | "readable" | "writable" | "writeable";
type GLOBALS = {
  [n: string]: G | boolean;
};
interface BaseConfig<Rules extends RulesRecord = RulesRecord> extends HasRules<Rules> {
  env?: ENV | undefined;
  extends?: string | string[] | undefined;
  globals?: GLOBALS | undefined;
  noInlineConfig?: boolean | undefined;
  overrides?: string[] | undefined;
  parser?: string | undefined;
  parserOptions?: ParserOptions | undefined;
  plugins?: string[] | undefined;
  processor?: string | undefined;
  reportUnusedDisableDirectives?: boolean | undefined;
  settings?: { [name: string]: any } | undefined;
}
interface Config<Rules extends RulesRecord = RulesRecord> extends BaseConfig<Rules> {
  ignorePatterns?: string | string[] | undefined;
  root?: boolean | undefined;
}