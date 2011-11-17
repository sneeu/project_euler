(ns euler21
  (:require [clojure.contrib.math]))

(defn is-divisor
  [n m]
  (if
    (= 0 (rem n m))
    m))

(defn divisors
  [n]
  (filter
    (fn [el] (not= el nil))
    (map
      (fn [m] (is-divisor n m))
      (range 1 (+ 1 (clojure.contrib.math/sqrt n))))))

(defn all-divisors
  [n]
  (let
    [left (divisors n)
     right (map (fn [m] (/ n m)) left)]
    (clojure.set/difference (clojure.set/union (set left) (set right)) #{n})))



(println (map (fn [n] {(apply + (all-divisors n)) n}) (range 10 20)))

;(println (apply + (all-divisors 100)))
