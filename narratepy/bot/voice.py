import re
import pyttsx3

from .data_obj import VoiceSettings

NO_MP3 = "No mp3 was created as the text contained 0 characters."


class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()

    @staticmethod
    def _rm_custom_emoji(text: str) -> str:
        """
        絵文字IDは読み上げないようにする
        :param text: オリジナルのテキスト
        :return: 絵文字IDを除去したテキスト
        """
        pattern = r"<:[a-zA-Z0-9_]+?:[0-9]+>"
        return re.sub(pattern, "", text)

    @staticmethod
    def _omit_code_block(text: str) -> str:
        """
        コードブロックを省略する
        :param text: オリジナルのテキスト
        :return: コードブロック省略したテキスト
        """
        pattern = r"`{3}.+?`{3}"
        return re.sub(pattern, "コードブロック省略", text, flags=re.DOTALL)

    @staticmethod
    def _omit_url(text: str) -> str:
        """
        URLを省略する
        :param text: オリジナルのテキスト
        :return: URLの省略したテキスト
        """
        pattern = r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
        return re.sub(pattern, "URL省略", text)

    @staticmethod
    def _rm_picture(text: str) -> str:
        """
        画像の読み上げを止める
        :param text: オリジナルのテキスト
        :return: 画像の読み上げを省略したテキスト
        """
        pattern = r".*(\.jpg|\.jpeg|\.gif|\.png|\.bmp)"
        return re.sub(pattern, "", text)

    @staticmethod
    def _rm_command(text: str) -> str:
        """
        コマンドの読み上げを止める
        :param text: オリジナルのテキスト
        :return: コマンドを省略したテキスト
        """
        return re.sub(r"^(!|\?|$|\.|>).*", "", text, flags=re.DOTALL)

    @staticmethod
    def _rm_mention(text: str) -> str:
        """
        メンションを除去する
        :param text: オリジナルのテキスト
        :return: メンションを省略したテキスト
        """
        pattern = r"<@\d+?>"
        return re.sub(pattern, "", text, flags=re.DOTALL)

    def _gen_mp3(self, msg: str, mp3_path: str, voice_settings: VoiceSettings):
        voices = self.engine.getProperty("voices")
        # self.engine.setProperty("voice", voices[voice_settings.voice].id)
        self.engine.setProperty("rate", voice_settings.rate)
        self.engine.save_to_file(msg, mp3_path)
        self.engine.runAndWait()
        print(f"save: {mp3_path}")

    def create_mp3(self, display_name: str, text: str, mp3_path: str, voice_settings: VoiceSettings):
        filters = [
            self._rm_custom_emoji, self._omit_code_block, self._omit_url,
            self._rm_picture, self._rm_command, self._rm_mention,
        ]
        for fx in filters:
            text = fx(text)
        if text:
            msg: str = f"{display_name}, {text}"
            self._gen_mp3(msg, mp3_path, voice_settings)
            return mp3_path
        return NO_MP3
