# 本地构建验证记录

- 已通过 `npm run build` 成功生成 Astro 静态站点；产物同时包含新首页、旧站归档和工程译文专题。
- 已直接打开 `dist/index.html`：导航、工程译文入口、旧站归档入口及浅色主题版式均正常显示。
- 已直接打开 `dist/engineering-cn/index.html`：专题页显示中文文章标题、原文链接及“非官方中文译文”声明；首篇自包含译文位于 `dist/engineering-cn/april-23-postmortem/index.html`。
- 首篇译文作为独立 HTML 保存，页面自身不依赖同级 `assets/` 目录。
