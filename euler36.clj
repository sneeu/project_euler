(defn is-palindrome [s]
  (= s (apply str (reverse s))))


(defn main []
  (apply +
         (filter #(and (is-palindrome (Integer/toString %)) (is-palindrome (Integer/toString % 2)))
         (range 1 1000000 2))))


(println (main))
