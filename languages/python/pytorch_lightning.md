---
marp: true
theme: default
paginate: true
style: |
    section::after {
        content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    }

    section.title h1 {
        font-size: 60px;
    }
    section.content h1 {
        position: absolute;
        left: 80px; top: 80px;
    }

---

<!-- _header: 2023/05/24 -->
<!-- _footer: Aoki Lab. -->
<!-- _class: invert title -->
<!-- _paginate: false -->

# PyTorch Lightning 入門
## Shion Yamadate

---

<!-- class: invert content -->

# Outline
本スライドでは，必要最低限の構成要素の説明を目的とする

<br>

- [Pytorch Lightning とは](#pytorch-lightning-とは)
  - [LightningDataModule](#lightningdatamodule)
  - [LightningModule](#lightningmodule)
  - [Trainer](#trainer)
- [備考：GitHub リポジトリ](#備考github-リポジトリ)

---

# PyTorch Lightning とは

- サードパーティ製のフレームワークで，PyTorch コードを整理して書ける

<br>

> PyTorch Lightning is the deep learning framework for professional AI researchers and machine learning engineers who need maximal flexibility without sacrificing performance at scale.

---

# PyTorch Lightning のメリット

- 可読性が高い
  - メソッド名などが事前に決められている
  - 定型文を省略
  - コードの共有が楽

- サイエンス以外の部分のコードがほぼゼロ
  - 精度向上・手法の追求に集中できる
  - テストが事前に用意されている

---

# PyTorch Lightning のインストール

- pip 経由
```sh
$ pip install pytorch-lightning
```

<br>

- Apple Sillicon (M1/M2/M3) Mac の場合，以下の環境変数を設定
```sh
GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
```

---

# LightningDataModule

<br>

- データを管理するために記載

```python
import pytorch_lightning as pl


class LitDataModule(pl.LightningDataModule):
    def prepare_data(self):
        # データのダウンロード

    def setup(self, stage: str):
        # stage に合わせてデータセットの用意

    def train_dataloader(self) -> DataLoader:
        # DataLoader を返す
```

---

# LightningModule

<br>

- `nn.Modules` に対する操作を記載

```python
import pytorch_lightning as pl


class LitModule(pl.LightningModule):
    def __init__(self, ...):
        # モデル（nn.Modules）の定義

    def training_step(self, batch, batch_idx) -> loss:
        # 訓練の定期

    def configure_optimizers(self) -> optimizer:
        # オプティマイザの定義
```

---

# Trainer

<br> 

- エンジニアリング部分を設定で自動化

```python
import pytorch_lightning as pl

from litmodule import LitModule
from litdatamodule import LitDataModule


model = LitModule()
data = LitDataModule()

trainer = pl.Trainer() # 必要に応じてフラグ指定
trainer.fit(model, data)
```

---

# LightningModule と Trainer の利点

<br>

- `.cuda()` や `.to(device)` が不要
  - 必要であれば `self.device` でアクセス可能
- `self.log()` でロギング

<br>

- モデルのモードの自動設定
- `grad`系，`.backward()`，`.step()` 処理の内在化
- エポック及びバッチでの，ループ処理の記述が不要

---

# 備考：GitHub リポジトリ

- [PyTorch Lightning](https://github.com/Lightning-AI/lightning/tree/master/src/pytorch_lightning) の公式リポジトリ

<br>

- [PyTorch Lightning テンプレ](https://github.com/pasca-l/pytorch-lightning-template)の自作リポジトリ
  - docker, poetry で環境構築を省略
  - 必要最低限のコードで実装したサンプル
  - 実験に重点を置いたテンプレ作成中

---

# 備考：本スライドについて

<br>

本スライドは [Marp](https://marp.app/) (Markdown Presentation Ecosystem) を用いて作成している
- [Marpit](https://marpit.marp.app/) フレームワークを利用
  - Markdown と CSS テーマから，静的 HTML と CSS で構成される slide deck に変換（Webページから PDF も作成可）
- [CommonMark](https://commonmark.org/) 仕様に従う
  - `---` をページ分割に使用
  - directive の拡張は可能（`marpit.use()` で markdown-it parser にプラグインを追加），同様な効果を`<style>`タグでも実現可能
- [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) 拡張機能や [Marp CLI](https://github.com/marp-team/marp-cli/) も提供している