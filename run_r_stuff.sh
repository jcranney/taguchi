file='database.txt'
rm $file
for n_states in $(seq 2 5)
do
for n_params in $(seq 2 20)
do
    echo '### n_params='$n_params 'n_states='$n_states >> $file
    echo "library(DoE.base); oa.design(nlevels=c("$(python -c 'print(str(['$n_states']*'$n_params')[1:-1])')"))" | R --vanilla --quiet 2>&1 | grep --after-context 1000 " A " >> $file
done
done