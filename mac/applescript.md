# AppleScript
https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html

MacOSを直接制御できる言語。

ちなみに、同じようなことがJSでできるJavaScript for Automation(JXA)というものもあるらしいが、日本語情報が少なそう。

## コード例：

指定のアプリケーションを起動

`activate application "Google Chrome"`

ブラウザで指定のurlを表示

`open location "https://google.com"`

通知センターに通知を出す

`display notification "notificationls" with title "title"`

## コマンドラインから実行：

`osascript -e 'コマンド'`

例：

`osascript -e 'display notification "test"'`


