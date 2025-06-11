# include general utilities
. `dirname $BASH_SOURCE[0]`/../utils.sh

# destinguish benchmark sizes
case $SIZE in
    small)
        N=1756
        ;;
    medium)
        N=7070 
        ;;
    large)
        N=13874 
        ;;
    xlarge)
        N=4000
        ;;
    custom)
        N=${N:=1000}
        echo "Custom problem size $N"     
        ;;
esac

N=$N                        # number of instructions of each type
O=`expr $N / 10`            # number of objects 
V=`expr $N / 4`             # number of variables


# create fact files as needed
#             | name | |entries| |       ranges        |
gen_fact_file   AddressOf  $N    $V $O
gen_fact_file   Assign  $N  $V $V
gen_fact_file      Load2      $N    $V $V
gen_fact_file      Store2     $N    $V $V

