#!\bin\bash

f3(){
	case $1 in
	     1)
	     	     echo "Ala ma kota"
	     	     ;;
	     2 | 3 | 4)
	     	     echo "Ala ma $1 koty"
	     	     ;;
	     5 | 6 | 7 | 8 | 9)
		     echo "Ala ma $1 kotów"
		     ;;
	     *)
		     echo "Ala ma ilosc kotow z poza zakresu (1-9)"
		     ;;
	esac	
}

f3 9 
f3 3
f3 1
f3 2
f3 4
f3 5
f3 6
f3 7
f3 8
f3 20
f3 a
