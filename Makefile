terrors: #ok
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
	@echo "\n"


t3e: #ok
	@echo "\n\033[1;34mTester 10: puzzle 3x3 easy manhattan \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy.txt -astar -manhattan
	@echo "\n\033[1;34mTester 10: puzzle 3x3 easy euclidean \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy.txt -astar -euclidean
	@echo "\n\033[1;34mTester 10: puzzle 3x3 easy misplaced \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy.txt -astar -misplaced
	@echo "\n\033[1;34mTester 10: puzzle 3x3 easy chebyshev \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy.txt -astar -chebyshev
	@echo "\n"


t3e3: #ok
	@echo "\n\033[1;34mTester 10: puzzle 3x3 easy3 manhattan \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy3.txt -astar -manhattan
	@echo "\n\033[1;34mTester 10: puzzle 3x3 easy3 euclidean \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy3.txt -astar -euclidean
	@echo "\n\033[1;34mTester 10: puzzle 3x3 easy3 misplaced \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy3.txt -astar -misplaced
	@echo "\n\033[1;34mTester 10: puzzle 3x3 easy3 chebyshev \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy3.txt -astar -chebyshev
	@echo "\n"


t3eNo: #ok
	@echo "\n\033[1;34mTester 10: puzzle 3x3 no solution manhattan \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy2.txt -astar -manhattan
	@echo "\n\033[1;34mTester 10: puzzle 3x3 no solution euclidean \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy2.txt -astar -euclidean
	@echo "\n\033[1;34mTester 10: puzzle 3x3 no solution misplaced \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy2.txt -astar -misplaced
	@echo "\n\033[1;34mTester 10: puzzle 3x3 no solution chebyshev \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_easy2.txt -astar -chebyshev
	@echo "\n"


t3m: #resolve, mas numero de passos gigantescos
	@echo "\n\033[1;34mTester 10: puzzle 3x3 medium manhattan \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_medium.txt -astar -manhattan
	@echo "\n\033[1;34mTester 10: puzzle 3x3 medium euclidean \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_medium.txt -astar -euclidean
	@echo "\n\033[1;34mTester 10: puzzle 3x3 medium misplaced \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_medium.txt -astar -misplaced
	@echo "\n\033[1;34mTester 10: puzzle 3x3 medium chebyshev \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_medium.txt -astar -chebyshev
	@echo "\n"


t3h: #resolve, mas numero de passos gigantescos
	@echo "\n\033[1;34mTester 10: puzzle 3x3 hard manhattan \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_hard.txt -astar -manhattan
	@echo "\n\033[1;34mTester 10: puzzle 3x3 hard euclidean \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_hard.txt -astar -euclidean
	@echo "\n\033[1;34mTester 10: puzzle 3x3 hard misplaced \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_hard.txt -astar -misplaced
	@echo "\n\033[1;34mTester 10: puzzle 3x3 hard chebyshev \033[0;00m"
	python3 main.py puzzles/npuzzle-3-1_hard.txt -astar -chebyshev
	@echo "\n"


t4: #ok
	@echo "\n\033[1;34mTester 10: puzzle 4x4 manhattan \033[0;00m"
	python3 main.py puzzles/npuzzle-4-1.txt -astar -manhattan
	@echo "\n\033[1;34mTester 10: puzzle 4x4 euclidean \033[0;00m"
	python3 main.py puzzles/npuzzle-4-1.txt -astar -euclidean
	@echo "\n\033[1;34mTester 10: puzzle 4x4 misplaced \033[0;00m"
	python3 main.py puzzles/npuzzle-4-1.txt -astar -misplaced
	@echo "\n\033[1;34mTester 10: puzzle 4x4 chebyshev \033[0;00m"
	python3 main.py puzzles/npuzzle-4-1.txt -astar -chebyshev
	@echo "\n\033[1;34mTester 10: puzzle 4x4 easy manhattan \033[0;00m"
	python3 main.py puzzles/npuzzle-4-1_easy.txt -astar -manhattan
	@echo "\n\033[1;34mTester 10: puzzle 4x4 easy euclidean \033[0;00m"
	python3 main.py puzzles/npuzzle-4-1_easy.txt -astar -euclidean
	@echo "\n\033[1;34mTester 10: puzzle 4x4 easy misplaced \033[0;00m"
	python3 main.py puzzles/npuzzle-4-1_easy.txt -astar -misplaced
	@echo "\n\033[1;34mTester 10: puzzle 4x4 easy chebyshev \033[0;00m"
	python3 main.py puzzles/npuzzle-4-1_easy.txt -astar -chebyshev
	@echo "\n"


