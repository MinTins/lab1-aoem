from timeit import Timer;


class TestTimer:

	@staticmethod
	def _Int(operation):
		code_frag = None;

		match operation:
			case "+":
				code_frag = ("a3 = a1+a2;a4 = a3+a1;a5 = a4+a2;a6 = a4+a5");

			case "-":
				code_frag = ("a3 = a1-a2;a4 = a3-a1;a5 = a4-a2;a6 = a4-a5");

			case "*":
				code_frag = ("a3 = a1*a2;a4 = a3*a1;a5 = a4*a2;a6 = a4*a5");

			case "//":
				code_frag = ("a3 = a1//a2;a4 = a3//a2;a5 = a1//a2;a6 = a3//a2;");

			case _:
				raise NotImplementedError(f"TestTimer | Int | {operation = }")

		return Timer(code_frag, globals={"a1": 45262, "a2": 100});

	@staticmethod
	def _Float(operation):
		code_frag = None;

		match operation:
			case "+":
				code_frag = ("a3 = a1+a2;a4 = a3+a1;a5 = a4+a2;a6 = a4+a5");

			case "-":
				code_frag = ("a3 = a1-a2;a4 = a3-a1;a5 = a4-a2;a6 = a4-a5");

			case "*":
				code_frag = ("a3 = a1*a2;a4 = a3*a1;a5 = a4*a2;a6 = a4*a5");

			case "/":
				code_frag = ("a3 = a1/a2;a4 = a3/a1;a5 = a1/a2;a6 = a3/a1");

			case _:
				raise NotImplementedError(f"TestTimer | Float | {operation = }")

		return Timer(code_frag, globals={"a1": 45262.0, "a2": 100.0});


	@staticmethod
	def _String(operation):
		code_frag = None;

		match operation:
			case "+":
				code_frag = ("a3 = a1+a2;a4 = a3+a1;a5 = a4+a2;a6 = a4+a5");

			case "*":
				code_frag = ("a3 = a1*b;a4 = a2*b;a5 = a3*b;a6 = a4*b");

			case _:
				raise NotImplementedError(f"TestTimer | String | {operation = }")

		return Timer(code_frag, globals={"a1": "A", "a2": "B","b":100});


	@staticmethod
	def _List(operation):
		code_frag = None;

		match operation:
			case "+":
				code_frag = ("a3 = a1+a2;a4 = a3+a1;a5 = a4+a2;a6 = a4+a5");

			case "*":
				code_frag = ("a3 = a1*b;a4 = a3*b;a5 = a3*b;a6 = a4*b");

			case _:
				raise NotImplementedError(f"TestTimer | List | {operation = }")

		return Timer(code_frag, globals={"a1": [0], "a2": [1], "b": 10});


	@staticmethod
	def _Dict(operation):
		code_frag = None;

		match operation:
			case "|":
				code_frag = ("a3 = a1|a2;a4 = a3|a1;a5 = a4|a2;a6 = a4|a5");

			case _:
				raise NotImplementedError(f"TestTimer | Dict | {operation = }")

		return Timer(code_frag, globals={"a1": {1:1,2:2,3:3}, "a2": {2:2}});


	
	@staticmethod
	def _Set(operation):
		code_frag = None;

		match operation:
			case "|":
				code_frag = ("a3 = a1|a2;a4 = a3|a1;a5 = a4|a2;a6 = a4|a5");

			case "&":
				code_frag = ("a3 = a1&a2;a4 = a3&a1;a5 = a4&a2;a6 = a4&a5");

			case "^":
				code_frag = ("a3 = a1^a2;a4 = a3^a1;a5 = a4^a2;a6 = a4^a5");

			case "-":
				code_frag = ("a3 = a1-a2;a4 = a3-a1;a5 = a4-a2;a6 = a4-a5");

			case _:
				raise NotImplementedError(f"TestTimer | Set | {operation = }")

		return Timer(code_frag, globals={"a1": {1,2,3}, "a2": {2}});


	@staticmethod
	def _Free():
		return Timer("pass", globals={});


	def _check_arrange(self, Time_obj):
		time_res = Time_obj.repeat(self.repeat, self.number)
		arrange = (sum(time_res)/self.repeat)/self.number

		return arrange


	def speed_test(self):
		check_list = {"Int": (self._Int,("+", "-", "*", "//")), 
		"Float": (self._Float, ("+", "-", "*", "/")),
		"String": (self._String,("+", "*")),
		"List": (self._List,("+", "*")),
		"Dict": (self._Dict, ("|")),
		"Set": (self._Set,("|", "&", "^", "-"))}

		free_cycle_time = self._check_arrange(self._Free())

		result_dict = {}

		for Type, (timer_gen,oper_group) in check_list.items():
			for operation in oper_group:
				result_dict[(Type, operation)] = self._check_arrange(timer_gen(operation)) - free_cycle_time;

		return result_dict


	def print_result(self, result_dict):

		min_value = min(result_dict.values())
		prev = None

		print("Type | ".ljust(1) + "Operation | ".ljust(45) + ("| Graph | ").ljust(55) + f"| percent %")

		for (Type, operation), time_res in result_dict.items():

			if prev != Type:
				prev = Type
				print("-"*119)

			res = Type.ljust(7) + operation.ljust(3) + ("#" * int(min_value*100//time_res)).ljust(102) + f"{round(min_value*100/time_res, 2)} %"
			print(res)

	def __init__(self, repeat=10, number=10000):
		self.repeat = repeat;
		self.number = number;



if __name__=="__main__":
	time_tester = TestTimer();
	res_dict = time_tester.speed_test()
	time_tester.print_result(res_dict)