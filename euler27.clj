(ns euler27
  (:require [clojure.contrib.lazy-seqs]))


(defn primes-less-equal-than [n]
  (take-while #(<= % n) clojure.contrib.lazy-seqs/primes))


(defn is-prime [n]
  (some #{n} (primes-less-equal-than n)))


(defn quadratic [a b n]
  (+ (* n n) (* a n) b))


(defn prime-solutions [a b]
  (take-while #(is-prime %)
    (map #(quadratic a b %) (range))))


(defn main []
  (let [
        as (range -999 999)
        bs (apply conj (primes-less-equal-than 999) (map #(* % -1) (primes-less-equal-than 999)))
        solution
          (last
            (sort
              (filter #(< 40 (first %))
                (for [a as b bs]
                  [(count (prime-solutions a b)) a b]))))]
    (* (nth solution 1) (nth solution 2))))


(println (main))
