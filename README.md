![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg) ![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue.svg) ![Discord Bot](https://img.shields.io/badge/Discord-Bot-purple.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

**\* English follows after Japanese**

# narratepy

このプロジェクトでは、Discordサーバーでユーザーのメッセージを自動的に音声で読み上げるbotを作成します。このbotはPythonを使用して開発されており、メッセージの読み上げには`pyttsx3`ライブラリを使用します。

## 使い方

### 1. 必要なパッケージのインストール
まず、このbotを実行するために必要なPythonパッケージをインストールします。

```shell
python -m pip install -r requirements.txt
```

### 2. .envファイルの作成
Discord botのトークンを環境変数として設定するために、`.env`ファイルを作成します。このファイルには以下の内容を含めます：

```shell
DISCORD_TOKEN=あなたのDiscord botトークン
```

### 3. Privileged Gateway Intentsをすべてオンにする
DiscordのDEVELOPER PORTALの作成したアプリケーションを選び、Botをクリックしてください。Privileged Gateway Intents内にあるトグルスイッチをすべてONの状態にしてください。


### 4. Botの起動
以下のコマンドを使用して、botを起動します：

```shell
python narratepy
```

## コマンド一覧

- `?join`: Botを音声チャンネルに接続します。
- `?bye`: Botを音声チャンネルから切断します。

## 注意点

- このbotは現在、テキストメッセージをそのまま読み上げます。これには絵文字ID、URL、コードブロックなども含まれます。それらを読み上げないようにするためには、`Voice`クラスのメソッドを適宜編集してください。
- デフォルトでは、音声ファイルは`./voice/`ディレクトリに一時的に保存され、botが終了するとそのディレクトリは削除されます。この動作を変更したい場合は、`main.py`を適宜編集してください。

## ライセンス
このプロジェクトはMITライセンスのもとで公開されています。詳細は`LICENSE`ファイルをご覧ください。


# narratepy \[English]

This project creates a bot that automatically reads aloud user messages on a Discord server. The bot is developed using Python and uses the `pyttsx3` library to read messages aloud.

## Usage

### 1. Install necessary packages
First, install the Python packages required to run this bot.

```shell
python -m pip install -r requirements.txt
```

### 2. Create .env file
Create a `.env` file to set the Discord bot token as an environment variable. Include the following content in this file:

```shell
DISCORD_TOKEN=your Discord bot token
```

### 3. Enable all Privileged Gateway Intents
Please select the application you have created in Discord's DEVELOPER PORTAL and click Bot. Please turn on all the toggle switches in Privileged Gateway Intents.

### 4. Launch the Bot
Use the following command to launch the bot:

```shell
python narratepy
```

## Command list

- `?join`: Connect the bot to your voice channel.
- `?bye`: Disconnect the bot from your voice channel.

## Note

- Currently, this bot reads text messages as is. This includes emoji IDs, URLs, code blocks, etc. To avoid reading them out, edit the methods of the `Voice` class as needed.
- By default, voice files are temporarily saved in the `./voice/` directory and this directory is deleted when the bot terminates. If you want to change this behavior, edit `main.py` as needed.

## License
This project is released under the MIT license. Please see the `LICENSE` file for details.
