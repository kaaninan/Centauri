; Auto-generated. Do not edit!


(cl:in-package emotiv_epoc-msg)


;//! \htmlinclude EEGFrame.msg.html

(cl:defclass <EEGFrame> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (accel_x
    :reader accel_x
    :initarg :accel_x
    :type cl:integer
    :initform 0)
   (accel_y
    :reader accel_y
    :initarg :accel_y
    :type cl:integer
    :initform 0)
   (channel_count
    :reader channel_count
    :initarg :channel_count
    :type cl:integer
    :initform 0)
   (channel_names
    :reader channel_names
    :initarg :channel_names
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (signals
    :reader signals
    :initarg :signals
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (qualities
    :reader qualities
    :initarg :qualities
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass EEGFrame (<EEGFrame>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EEGFrame>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EEGFrame)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name emotiv_epoc-msg:<EEGFrame> is deprecated: use emotiv_epoc-msg:EEGFrame instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <EEGFrame>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader emotiv_epoc-msg:header-val is deprecated.  Use emotiv_epoc-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'accel_x-val :lambda-list '(m))
(cl:defmethod accel_x-val ((m <EEGFrame>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader emotiv_epoc-msg:accel_x-val is deprecated.  Use emotiv_epoc-msg:accel_x instead.")
  (accel_x m))

(cl:ensure-generic-function 'accel_y-val :lambda-list '(m))
(cl:defmethod accel_y-val ((m <EEGFrame>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader emotiv_epoc-msg:accel_y-val is deprecated.  Use emotiv_epoc-msg:accel_y instead.")
  (accel_y m))

(cl:ensure-generic-function 'channel_count-val :lambda-list '(m))
(cl:defmethod channel_count-val ((m <EEGFrame>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader emotiv_epoc-msg:channel_count-val is deprecated.  Use emotiv_epoc-msg:channel_count instead.")
  (channel_count m))

(cl:ensure-generic-function 'channel_names-val :lambda-list '(m))
(cl:defmethod channel_names-val ((m <EEGFrame>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader emotiv_epoc-msg:channel_names-val is deprecated.  Use emotiv_epoc-msg:channel_names instead.")
  (channel_names m))

(cl:ensure-generic-function 'signals-val :lambda-list '(m))
(cl:defmethod signals-val ((m <EEGFrame>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader emotiv_epoc-msg:signals-val is deprecated.  Use emotiv_epoc-msg:signals instead.")
  (signals m))

(cl:ensure-generic-function 'qualities-val :lambda-list '(m))
(cl:defmethod qualities-val ((m <EEGFrame>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader emotiv_epoc-msg:qualities-val is deprecated.  Use emotiv_epoc-msg:qualities instead.")
  (qualities m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EEGFrame>) ostream)
  "Serializes a message object of type '<EEGFrame>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'accel_x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'accel_x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'accel_x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'accel_x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'accel_y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'accel_y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'accel_y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'accel_y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'channel_count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'channel_count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'channel_count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'channel_count)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'channel_names))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'channel_names))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'signals))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'signals))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'qualities))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'qualities))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EEGFrame>) istream)
  "Deserializes a message object of type '<EEGFrame>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'accel_x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'accel_x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'accel_x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'accel_x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'accel_y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'accel_y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'accel_y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'accel_y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'channel_count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'channel_count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'channel_count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'channel_count)) (cl:read-byte istream))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'channel_names) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'channel_names)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'signals) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'signals)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'qualities) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'qualities)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EEGFrame>)))
  "Returns string type for a message object of type '<EEGFrame>"
  "emotiv_epoc/EEGFrame")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EEGFrame)))
  "Returns string type for a message object of type 'EEGFrame"
  "emotiv_epoc/EEGFrame")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EEGFrame>)))
  "Returns md5sum for a message object of type '<EEGFrame>"
  "86134851c3839c35d0c7eb7049a290b2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EEGFrame)))
  "Returns md5sum for a message object of type 'EEGFrame"
  "86134851c3839c35d0c7eb7049a290b2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EEGFrame>)))
  "Returns full string definition for message of type '<EEGFrame>"
  (cl:format cl:nil "Header header~%uint32 accel_x~%uint32 accel_y~%~%uint32 channel_count~%string[] channel_names~%uint32[] signals~%uint32[] qualities~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EEGFrame)))
  "Returns full string definition for message of type 'EEGFrame"
  (cl:format cl:nil "Header header~%uint32 accel_x~%uint32 accel_y~%~%uint32 channel_count~%string[] channel_names~%uint32[] signals~%uint32[] qualities~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EEGFrame>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'channel_names) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'signals) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'qualities) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EEGFrame>))
  "Converts a ROS message object to a list"
  (cl:list 'EEGFrame
    (cl:cons ':header (header msg))
    (cl:cons ':accel_x (accel_x msg))
    (cl:cons ':accel_y (accel_y msg))
    (cl:cons ':channel_count (channel_count msg))
    (cl:cons ':channel_names (channel_names msg))
    (cl:cons ':signals (signals msg))
    (cl:cons ':qualities (qualities msg))
))
