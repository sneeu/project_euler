(defn pow [x n]
  (apply * (repeat n x)))


(def the-pow 5)
(def the-min 2)
(def the-max (+ (* the-pow (pow 9 the-pow)) 1))
(def the-range (range the-min the-max))


(defn digits [n]
  (map #(Integer/parseInt (str %)) (str n)))


(println (apply + (for [x the-range
               :when (= x (apply + (map #(pow % the-pow) (digits x))))]
           x)))
