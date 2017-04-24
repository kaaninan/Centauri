;; Auto-generated. Do not edit!


(when (boundp 'emotiv_epoc::EEGFrame)
  (if (not (find-package "EMOTIV_EPOC"))
    (make-package "EMOTIV_EPOC"))
  (shadow 'EEGFrame (find-package "EMOTIV_EPOC")))
(unless (find-package "EMOTIV_EPOC::EEGFRAME")
  (make-package "EMOTIV_EPOC::EEGFRAME"))

(in-package "ROS")
;;//! \htmlinclude EEGFrame.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass emotiv_epoc::EEGFrame
  :super ros::object
  :slots (_header _accel_x _accel_y _channel_count _channel_names _signals _qualities ))

(defmethod emotiv_epoc::EEGFrame
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:accel_x __accel_x) 0)
    ((:accel_y __accel_y) 0)
    ((:channel_count __channel_count) 0)
    ((:channel_names __channel_names) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:signals __signals) (make-array 0 :initial-element 0 :element-type :integer))
    ((:qualities __qualities) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _header __header)
   (setq _accel_x (round __accel_x))
   (setq _accel_y (round __accel_y))
   (setq _channel_count (round __channel_count))
   (setq _channel_names __channel_names)
   (setq _signals __signals)
   (setq _qualities __qualities)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:accel_x
   (&optional __accel_x)
   (if __accel_x (setq _accel_x __accel_x)) _accel_x)
  (:accel_y
   (&optional __accel_y)
   (if __accel_y (setq _accel_y __accel_y)) _accel_y)
  (:channel_count
   (&optional __channel_count)
   (if __channel_count (setq _channel_count __channel_count)) _channel_count)
  (:channel_names
   (&optional __channel_names)
   (if __channel_names (setq _channel_names __channel_names)) _channel_names)
  (:signals
   (&optional __signals)
   (if __signals (setq _signals __signals)) _signals)
  (:qualities
   (&optional __qualities)
   (if __qualities (setq _qualities __qualities)) _qualities)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _accel_x
    4
    ;; int32 _accel_y
    4
    ;; uint32 _channel_count
    4
    ;; string[] _channel_names
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _channel_names)) 4
    ;; int32[] _signals
    (* 4    (length _signals)) 4
    ;; int32[] _qualities
    (* 4    (length _qualities)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _accel_x
       (write-long _accel_x s)
     ;; int32 _accel_y
       (write-long _accel_y s)
     ;; uint32 _channel_count
       (write-long _channel_count s)
     ;; string[] _channel_names
     (write-long (length _channel_names) s)
     (dolist (elem _channel_names)
       (write-long (length elem) s) (princ elem s)
       )
     ;; int32[] _signals
     (write-long (length _signals) s)
     (dotimes (i (length _signals))
       (write-long (elt _signals i) s)
       )
     ;; int32[] _qualities
     (write-long (length _qualities) s)
     (dotimes (i (length _qualities))
       (write-long (elt _qualities i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _accel_x
     (setq _accel_x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _accel_y
     (setq _accel_y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _channel_count
     (setq _channel_count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string[] _channel_names
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _channel_names (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _channel_names i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; int32[] _signals
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _signals (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _signals i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _qualities
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _qualities (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _qualities i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get emotiv_epoc::EEGFrame :md5sum-) "92a93661fa971fb7494f0877c88d2361")
(setf (get emotiv_epoc::EEGFrame :datatype-) "emotiv_epoc/EEGFrame")
(setf (get emotiv_epoc::EEGFrame :definition-)
      "Header header
int32 accel_x
int32 accel_y

uint32 channel_count
string[] channel_names
int32[] signals
int32[] qualities

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

")



(provide :emotiv_epoc/EEGFrame "92a93661fa971fb7494f0877c88d2361")


