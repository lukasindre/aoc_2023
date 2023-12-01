#!/bin/sh

for i in 0{1..9} {10..25}
do
  mkdir $i
  cd $i
  touch input.in
  cat << EOF > puzzle.py
class Solution:
    def __init__(self, input_file: str = "input.in") -> None:
        with open(input_file, "r") as f:
            self.data = f.readlines()
    
    def one(self) -> None:
        pass

    def two(self) -> None:
        pass


if __name__ == "__main__":
    s = Solution()
    s.one()
    s.two()
EOF
  cd ..
done
