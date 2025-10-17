
class App:
    def __init__(self, name):
        self.name = name 
        self.todos = []

    def todo_list(self):
        if not self.todos:
            print("You have nothing planned")
        else:
            print(f"\n{self.name}, your plans to do:")
            for i, todo in enumerate(self.todos, 1):
                print(f"{i}. {todo}")

    def create_todo(self):
        todo = input("Input your plan: ")
        if todo.strip():
            self.todos.append(todo)
            print("Your plan was added")
        else:
            print("Empty plan not added")

    def run(self):
        print(f"Welcome {self.name}:)\n")
        while True:
            print("Menu:")
            print("Show my plans ==> 1")
            print("I want to add plans ==> 2")
            print("Exit ==> ex")

            choice = input("Choose option==> ")
            if choice == "1":
                self.todo_list()   
            elif choice == "2":
                self.create_todo()
            elif choice == "ex":
                print("Goodbye!")
                break
            else:
                print("Invalid choice\n")


if __name__ == '__main__':
    user_name = input("your name: ")
    app = App(user_name)
    app.run()
