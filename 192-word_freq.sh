perl -ne 'while(/(\w+)/g) { print "$1\n" }' words.txt | sort | uniq -c | awk '{ print $2, $1 }' | sort -nr -k2,2
