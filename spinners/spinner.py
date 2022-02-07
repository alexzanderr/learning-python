from threading import Thread
from time import sleep


frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

class Task():
	def __init__(self, seconds) -> None:
		self.done = 0
		self.seconds = seconds

	def is_done(self):
		return self.done

	def run_task(self):
		for _ in range(self.seconds):
			sleep(1)
		self.done = 1

class Spinner():
	def __init__(self) -> None:
		self.key_frame = 0
	
	def next(self):
		self.key_frame += 1
		return frames[self.key_frame % len(frames)]

def func():
	for i in range(5):
		print(i)
		sleep(1)

def main():
	task1 = Task(5)
	task2 = Task(3)

	thread1 = Thread(target=(task1.run_task))
	thread2 = Thread(target=(task2.run_task))

	thread1.start()
	thread2.start()

	spinner = Spinner()

	while 1:
		line = ""
		total_done = 0
		if task1.is_done():
			line += f"Done{' ' * 5}"
			total_done += 1
		else:
			line += f"{spinner.next()}{' ' * 5}"

		if task2.is_done() == 0:
			line += spinner.next()
			total_done += 1
		else:
			line += "Done"

		print(line, end='\r')

		if total_done == 2:
			break
		sleep(0.1)


if __name__ == '__main__':
	main()
