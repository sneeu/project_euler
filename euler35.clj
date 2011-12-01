(ns euler35
  (:require clojure.contrib.lazy-seqs
            clojure.set))


(def primes (set (map str (take-while #(< % 1000000) clojure.contrib.lazy-seqs/primes))))


(defn cycles [s]
  (for [i (range 0 (count s))]
    (apply str (take (count s) (drop i (str s s))))))


(def cyclical-primes
  (filter #(let [cy (set (cycles %))]
             (=
               (count (clojure.set/intersection cy primes))
               (count cy)))
          primes))


(println (count cyclical-primes))
