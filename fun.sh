#!\bin\bash

f1() {

	echo "wywołano z $# parametrami, parametry to: $@"
	[ $# -lt 2 ] && return;
	echo -e "drugi: $2\npierwszy: $1"

	# albo kolejnych w pętli
	for a in "$@"; do echo $a; done

	# lub z użyciem polecenia shift
	for i in `seq 1 $#`; do
		echo $1
		shift # powoduje zapomnienie $1
		# i przenumerowanie argumentów pozycyjnych o 1
		# wpływa na wartości $@ $# itp
	done
	# funkcja może zwracać tylko wartość numeryczną -- tzw kod powrotu
	return 83
}


f1 a "c" d
