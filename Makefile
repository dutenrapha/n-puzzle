t0:
	@echo "\n\033[1;34mTester 1: puzzle 1x1 \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_error_1x1.txt
	@echo "\n\033[1;34mTester 2: puzzle with char \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_error_char.txt
	@echo "\n\033[1;34mTester 3: puzzle not square \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_error_not_square.txt
	@echo "\n\033[1;34mTester 4: puzzle with numbers not unique \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_error_not_unique.txt
	@echo "\n\033[1;34mTester 5: puzzle out of range \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_error_range.txt
	@echo "\n\033[1;34mTester 6: puzzle with size incompatible \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_error_size.txt
	@echo "\n\033[1;34mTester 7: puzzle 3x3 nok \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1.txt -astar
	@echo "\n\033[1;34mTester 8: puzzle 4x4 ok \033[0;00m"
	#python3 main.py puzzles/npuzzle-4-1.txt -astar
	@echo "\n\033[1;34mTester 9: puzzle 4x4 ok \033[0;00m"
	#python3 main.py puzzles/npuzzle-4-1b.txt -astar
	@echo "\n\033[1;34mTester 10: puzzle 3x3 easy \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy.txt -astar
	@echo "\n\033[1;34mTester 11: puzzle 3x3 medium \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_medium.txt -astar
	@echo "\n\033[1;34mTester 12: puzzle 3x3 hard \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_hard.txt -astar
	@echo "\n\033[1;34mTester 13: puzzle 3x3 easy2 \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy2.txt -astar
	@echo "\n"
