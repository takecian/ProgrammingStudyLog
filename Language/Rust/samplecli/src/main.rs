use samplecli::*;
use clap::{App, Arg};

fn main() {
    println!("Hello, world!");

    let app = App::new("sample cli")
        .version("0.1.0") // バージョン情報
        .author("myname <myname@mail.com>") // 作者情報
        .about("Clap Example CLI") // このアプリについて
        .arg(
            Arg::with_name("flg") // フラグを定義
                .help("sample flag") // ヘルプメッセージ
                .short("f") // ショートコマンド
                .long("flag"), // ロングコマンド
        )
        .arg(
            Arg::with_name("opt") // オプションを定義
                .help("sample option") // ヘルプメッセージ
                .short("o") // ショートコマンド
                .long("opt") // ロングコマンド
                .takes_value(true), // 値を持つことを定義
        );
    let matches = app.get_matches();
    // optが指定されていれば値を表示
    if let Some(o) = matches.value_of("opt") {
        println!("Value for opt: {}", o);
    }

    // flgのON/OFFで表示するメッセージを切り替え
    println!(
        "flg is {}",
        if matches.is_present("flg") {
            "ON"
        } else {
            "OFF"
        }
    );

    input!{
        n: usize,
        m: usize,
    };

    println!("{}", n);
}
