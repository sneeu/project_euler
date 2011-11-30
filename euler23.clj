(require 'clojure.set)


(defn sum [ns]
  (apply + ns))


(defn is-factor [f n]
  (= 0 (rem n f)))


(defn factors [n]
  (filter
    #(is-factor %1 n)
    (range 1 n)))


(defn is-abundent [n]
  (< n (apply + (factors n))))


(defn two-sums [ns]
  (set (for [x ns y ns] (+ x y))))

(defn main [nmax]
  (let [ns (set (range 1 nmax))
        abundents (filter is-abundent (range 1 nmax))
        the-two-sums (two-sums abundents)
        not-two-sums (clojure.set/difference ns the-two-sums)]
    (sum not-two-sums)))


(println (main 28124))


;(println (sum (not-two-sums
                ;(filter is-abundent (range 1 28124)))))
;(println (two-sums (filter is-abundent (range 1 20))))
