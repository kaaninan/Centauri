;; Auto-generated. Do not edit!


(when (boundp 'emotiv_epoc::ChangeFrequency)
  (if (not (find-package "EMOTIV_EPOC"))
    (make-package "EMOTIV_EPOC"))
  (shadow 'ChangeFrequency (find-package "EMOTIV_EPOC")))
(unless (find-package "EMOTIV_EPOC::CHANGEFREQUENCY")
  (make-package "EMOTIV_EPOC::CHANGEFREQUENCY"))
(unless (find-package "EMOTIV_EPOC::CHANGEFREQUENCYREQUEST")
  (make-package "EMOTIV_EPOC::CHANGEFREQUENCYREQUEST"))
(unless (find-package "EMOTIV_EPOC::CHANGEFREQUENCYRESPONSE")
  (make-package "EMOTIV_EPOC::CHANGEFREQUENCYRESPONSE"))

(in-package "ROS")





(defclass emotiv_epoc::ChangeFrequencyRequest
  :super ros::object
  :slots (_frequency ))

(defmethod emotiv_epoc::ChangeFrequencyRequest
  (:init
   (&key
    ((:frequency __frequency) 0)
    )
   (send-super :init)
   (setq _frequency (round __frequency))
   self)
  (:frequency
   (&optional __frequency)
   (if __frequency (setq _frequency __frequency)) _frequency)
  (:serialization-length
   ()
   (+
    ;; uint32 _frequency
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _frequency
       (write-long _frequency s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _frequency
     (setq _frequency (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass emotiv_epoc::ChangeFrequencyResponse
  :super ros::object
  :slots ())

(defmethod emotiv_epoc::ChangeFrequencyResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass emotiv_epoc::ChangeFrequency
  :super ros::object
  :slots ())

(setf (get emotiv_epoc::ChangeFrequency :md5sum-) "73ffa65309f649b8b694f03ce8799567")
(setf (get emotiv_epoc::ChangeFrequency :datatype-) "emotiv_epoc/ChangeFrequency")
(setf (get emotiv_epoc::ChangeFrequency :request) emotiv_epoc::ChangeFrequencyRequest)
(setf (get emotiv_epoc::ChangeFrequency :response) emotiv_epoc::ChangeFrequencyResponse)

(defmethod emotiv_epoc::ChangeFrequencyRequest
  (:response () (instance emotiv_epoc::ChangeFrequencyResponse :init)))

(setf (get emotiv_epoc::ChangeFrequencyRequest :md5sum-) "73ffa65309f649b8b694f03ce8799567")
(setf (get emotiv_epoc::ChangeFrequencyRequest :datatype-) "emotiv_epoc/ChangeFrequencyRequest")
(setf (get emotiv_epoc::ChangeFrequencyRequest :definition-)
      "uint32 frequency
---

")

(setf (get emotiv_epoc::ChangeFrequencyResponse :md5sum-) "73ffa65309f649b8b694f03ce8799567")
(setf (get emotiv_epoc::ChangeFrequencyResponse :datatype-) "emotiv_epoc/ChangeFrequencyResponse")
(setf (get emotiv_epoc::ChangeFrequencyResponse :definition-)
      "uint32 frequency
---

")



(provide :emotiv_epoc/ChangeFrequency "73ffa65309f649b8b694f03ce8799567")


