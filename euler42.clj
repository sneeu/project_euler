(ns euler42
  (:require [clojure.string]))


(def words
  (clojure.string/split
    (clojure.string/replace
      (slurp "words.txt")
      #"\"" "")
    #","))


(defn triangle [n]
  (/ (* n (+ n 1)) 2))


(defn sum [coll]
  (reduce + coll))


(defn score-word [word]
  (sum
    (map #(- (int %1) 64) word)))


(def scores
  (map score-word words))


(def triangles
  (set
    (for
      [t (range) :while (< (triangle t) (apply max scores))]
      (triangle t))))


(println (count (filter #(triangles %1) scores)))
