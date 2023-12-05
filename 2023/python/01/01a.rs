use std::env;
use std::fs::File;
use std::io;
use std::io::prelude::*;

fn get_sum_from_file(filename: &str) -> io::Result<()> {
    let file = File::open(&filename)?;

    let reader = io::BufReader::new(file);

    let mut sum = 0;

    for line in reader.lines() {
        let line = line?;
        
    }

    Ok(())
}

fn main() {
    let filename = env::args().nth(1).expect("Please supply input filename.");

    let _ =  get_sum_from_file(&filename).expect("Error");

}

