#[macro_export]
macro_rules! input {
    (source = $s:expr, $($r:tt)*) => {
        let mut iter = $s.split_whitespace();
        let mut next = || { iter.next().unwrap() };
        input_inner!{next, $($r)*}
    };
    ($($r:tt)*) => {
        let stdin = std::io::stdin();
        let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock()));
        let mut next = move || -> String{
            bytes
                .by_ref()
                .map(|r|r.unwrap() as char)
                .skip_while(|c|c.is_whitespace())
                .take_while(|c|!c.is_whitespace())
                .collect()
        };
        input_inner!{next, $($r)*}
    };
}

#[macro_export]
macro_rules! input_inner {
    ($next:expr) => {};
    ($next:expr, ) => {};

    ($next:expr, $var:ident : $t:tt $($r:tt)*) => {
        let $var = read_value!($next, $t);
        input_inner!{$next $($r)*}
    };
}

#[macro_export]
macro_rules! read_value {
    ($next:expr, ( $($t:tt),* )) => {
        ( $(read_value!($next, $t)),* )
    };

    ($next:expr, [ $t:tt ; $len:expr ]) => {
        (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>()
    };

    ($next:expr, chars) => {
        read_value!($next, String).chars().collect::<Vec<char>>()
    };

    ($next:expr, usize1) => {
        read_value!($next, usize) - 1
    };

    ($next:expr, $t:ty) => {
        $next().parse::<$t>().expect("Parse error")
    };
}

fn main() {
    input!{
        h: usize,
        w: usize,
        mat: [[i32; w]; h],
    }
    let mut rows: Vec<i32> = vec!();
    for row in &mat {
        let sum = row.iter().sum();
        rows.push(sum);
    }
    // println!("{:?}", rows);

    let mut columns: Vec<i32> = vec!();
    for c in 0..w {
        let mut sum: i32 = 0;
        for row in &mat {
            sum += row[c];
        }
        columns.push(sum);
    }
    // println!("{:?}", columns);

    let mut ans: Vec<Vec<i32>> = vec!();
    for row in 0..h {
        let mut row_ans: Vec<i32> = vec!();
        for col in 0..w {
            row_ans.push(columns[col] + rows[row] - mat[row][col]);
        }
        ans.push(row_ans);
    }
    for row in &ans {
        for val in row {
            print!("{:?} ", val);
        }
        println!("");
    }
}
