(defn is-factor [f n]
  (if (= 0 (rem n f))
    f
    0))


(defn factors [n]
  (filter
    (fn [n] (not (= n 0)))
    (map (fn [f] (is-factor f n)) (range 1 n))))


(defn d [n]
  (apply + (factors n)))


(defn pairs [ns]
  (map (fn [n] [n (d n)]) ns))


(defn main2 []
  (let [the-pairs (pairs (range 1 10001))]
    (filter
      (fn [i] (not (= i nil)))
      (map (fn [e] (some #{[(second e) (first e)]} the-pairs)) the-pairs))))


(defn summer []
  (let [the-pairs (main2)]
    (apply + (map
      first
      (filter
        (fn [pair] (not (= (first pair) (second pair))))
        the-pairs)))))


(println (summer))
