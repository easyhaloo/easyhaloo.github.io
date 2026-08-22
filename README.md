# easyhaloo.github.io

这是 `easyhaloo.github.io` 的 Astro 静态博客主站。站点保留旧 Hexo 生成内容作为 `/legacy/` 历史归档，并将经过本地 CLI Agent 验证的 Anthropic Engineering 中文镜像发布到 `/engineering-cn/`。

## 本地开发

```bash
npm install
npm run dev
npm run build
```

GitHub Actions 会在 `master` 分支收到提交后构建 `dist/` 并部署到 GitHub Pages。

## 内容结构

| 路径 | 用途 |
|---|---|
| `src/` | Astro 主站页面与全局布局。 |
| `public/legacy/` | 从原 Hexo 静态站迁移的历史文章、资源、分类和标签。 |
| `public/engineering-cn/` | 经验证的自包含中文工程译文及其专题索引。 |
| `.automation/anthropic-engineering-publish.json` | 本地 CLI Agent 调用发布辅助脚本时使用的 Astro 目标配置。 |

## 发布中文工程译文

先使用 `anthropic-engineering-zh-sync` Skill 完成文章发现、抓取、中文转写、保真渲染与资源验证。确认文章目录含有 `metadata.json` 与 `zh-CN-standalone.html` 后，在博客仓库运行：

```bash
python3 /path/to/anthropic-engineering-zh-sync/scripts/publish_to_astro.py \
  --config .automation/anthropic-engineering-publish.json \
  --article-dir /path/to/completed-article \
  --build --commit --push
```

该命令仅暂存并提交生成的 `public/engineering-cn/` 文章及其索引。推送会触发 GitHub Pages 部署。公开发布前，操作者必须确认拥有必要的翻译、转载与媒体使用授权，并保留原文链接及“非官方中文译文”说明。
