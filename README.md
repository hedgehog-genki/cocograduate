# アプリケーションの概要

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">これまでアップしてきた動画、アーカイブのサムネを使用してモザイクアートを作成して、動画にしました。<br><br>I will never forget the contributions and intentions you have made.<a href="https://twitter.com/hashtag/%E6%A1%90%E7%94%9F%E3%82%B3%E3%82%B3?src=hash&amp;ref_src=twsrc%5Etfw">#桐生ココ</a><a href="https://twitter.com/hashtag/%E3%81%BF%E3%81%8B%E3%81%98%E7%B5%B5?src=hash&amp;ref_src=twsrc%5Etfw">#みかじ絵</a> <a href="https://twitter.com/hashtag/%E6%A1%90%E7%94%9F%E3%82%B3%E3%82%B3%E5%8D%92%E6%A5%ADLIVE?src=hash&amp;ref_src=twsrc%5Etfw">#桐生ココ卒業LIVE</a><a href="https://twitter.com/hashtag/GoodbyeCoco?src=hash&amp;ref_src=twsrc%5Etfw">#GoodbyeCoco</a> <a href="https://t.co/SHEWwZYZJ6">pic.twitter.com/SHEWwZYZJ6</a></p>&mdash; ハリネズミの日記🥟ねねちのファンサイト公開中 (@hedgehog_nene) <a href="https://twitter.com/hedgehog_nene/status/1410585743332843528?ref_src=twsrc%5Etfw">July 1, 2021</a></blockquote>
Vtuberプロダクションのホロライブ所属の桐生ココさん2021/7/1に卒業することになり、同日卒業LIVEが行われました。
卒業LIVEに合わせて、モザイクアートと動画を作成しました。
本アプリケーションではモザイクアートで使用する画像を取得するアプリケーションとなっています。

こちらにも制作背景などを掲載しています。<br>
https://qiita.com/hedgehog-genki/items/c32df2fd1b241ab8ba1c

## 制作背景

桐生ココさんの卒業が決まってから、ファンアート（ファンが自主的に制作するイラストや動画）がTwitterでアップされているのを見て、<br>
自分も何か作成して、少しでも多くのファンに桐生ココさんのこれまでの軌跡が伝われば良いなと思い、作成に至りました。

## 使用技術

Python

## 工夫したポイント
### シンプルなコーディング
2021/7/1の午前中に思い立って、同日の夜２２時に動画を公開したので、本アプリのコーディングは実質5時間ほどで仕上げました。<br>
そのため、必要最低限の情報を取得するコーディングを意識して、作業時間を可能な限り、削減しました。<br>
また、今回はファンアートの場合、掲載許可が必要になるため工数の問題から、YouTube桐生ココさんのチャンネルのサムネイル画像をモザイクアートに使用することにしました。<br>

## 課題・今後実装したい機能
### ファンアートもモザイクアートに使用したかった
上述の通り、本アプリではYouTubeのサムネイルの取得に特化しています。<br>
今回の制作背景を鑑みると、ファンアートを使用したいと考えていましたが、工数の観点からYouTubeのサムネイルに特化することにしました。<br>
今後、同じようにモザイクアートを使用する場合は、ファンアートも使用したいと考えています。

### ファンアートを使用する場合の、使用許可取得の効率化
モザイクアートには大量の画像が必要になるため、ファンアート一つに対して、毎度使用許可をとっていると、工数がかかりすぎるため、<br>
ファンアートをモザイクアートに使用する場合、使用許可取得を効率化するためのプラットフォームが必要ではないかと考えます。
