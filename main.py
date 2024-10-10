import tkinter, argparse, os
from labels import TKLabels
from calculations import ThirdOrderMatrix, VectorMatrix

def render_ui():
  root = tkinter.Tk()
  root.title('Решение систем линейных уравнений')
  root.geometry('600x300')
  root.resizable(width = False, height = False)

  def calculate():
    matrix = ThirdOrderMatrix([
      [int(labels.matrix_1_entry.get()), int(labels.matrix_2_entry.get()), int(labels.matrix_3_entry.get())],
      [int(labels.matrix_4_entry.get()), int(labels.matrix_5_entry.get()), int(labels.matrix_6_entry.get())],
      [int(labels.matrix_7_entry.get()), int(labels.matrix_8_entry.get()), int(labels.matrix_9_entry.get())]
    ])
    
    vector = VectorMatrix(
      [int(labels.matrix_10_entry.get()), int(labels.matrix_11_entry.get()), int(labels.matrix_12_entry.get())]
    )
    
    result = matrix.cramer_calculate(vector)
    
    labels.result.configure(text=f"x = {result.get('x')}\ny = {result.get('y')}\nz = {result.get('z')}")
    
  labels = TKLabels(root, calculate)

  root.mainloop()

def render_console():
  os.system('cls' if os.name == 'nt' else 'clear')
  
  while True:
    print('\n\nВведите элементы матрицы A:\n')
    matrix = ThirdOrderMatrix([
      [int(input("А11: ")), int(input("А12: ")), int(input("А13: "))],
      [int(input("А21: ")), int(input("А22: ")), int(input("А23: "))],
      [int(input("A31: ")), int(input("А32: ")), int(input("А33: "))]
    ])
    
    print('\n\nВведите элементы вектора-столбца B:\n')
    vector = VectorMatrix(
      [int(input("В1: ")), int(input("В2: ")), int(input("В3: "))]
    )
    
    result = matrix.cramer_method(vector)
    result2 = matrix.gauss_method(vector)
    print(f"\nОтвет по методу Крамера:\nx = {result.get('x')}\ny = {result.get('y')}\nz = {result.get('z')}")
    print(f"\nОтвет по методу Гаусса:\nx = {result2.get('x')}\ny = {result2.get('y')}\nz = {result2.get('z')}")

parser = argparse.ArgumentParser()
parser.add_argument("-ui", "--ui", required=False, default=False, action='store_true')
args = parser.parse_args()

if args.ui:
  render_ui()
else:
  render_console()
