; Auto-generated. Do not edit!


(cl:in-package emotiv_epoc-srv)


;//! \htmlinclude ChangeFrequency-request.msg.html

(cl:defclass <ChangeFrequency-request> (roslisp-msg-protocol:ros-message)
  ((frequency
    :reader frequency
    :initarg :frequency
    :type cl:integer
    :initform 0))
)

(cl:defclass ChangeFrequency-request (<ChangeFrequency-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangeFrequency-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangeFrequency-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name emotiv_epoc-srv:<ChangeFrequency-request> is deprecated: use emotiv_epoc-srv:ChangeFrequency-request instead.")))

(cl:ensure-generic-function 'frequency-val :lambda-list '(m))
(cl:defmethod frequency-val ((m <ChangeFrequency-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader emotiv_epoc-srv:frequency-val is deprecated.  Use emotiv_epoc-srv:frequency instead.")
  (frequency m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangeFrequency-request>) ostream)
  "Serializes a message object of type '<ChangeFrequency-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'frequency)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'frequency)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'frequency)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'frequency)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangeFrequency-request>) istream)
  "Deserializes a message object of type '<ChangeFrequency-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'frequency)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'frequency)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'frequency)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'frequency)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangeFrequency-request>)))
  "Returns string type for a service object of type '<ChangeFrequency-request>"
  "emotiv_epoc/ChangeFrequencyRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeFrequency-request)))
  "Returns string type for a service object of type 'ChangeFrequency-request"
  "emotiv_epoc/ChangeFrequencyRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangeFrequency-request>)))
  "Returns md5sum for a message object of type '<ChangeFrequency-request>"
  "73ffa65309f649b8b694f03ce8799567")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangeFrequency-request)))
  "Returns md5sum for a message object of type 'ChangeFrequency-request"
  "73ffa65309f649b8b694f03ce8799567")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangeFrequency-request>)))
  "Returns full string definition for message of type '<ChangeFrequency-request>"
  (cl:format cl:nil "uint32 frequency~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangeFrequency-request)))
  "Returns full string definition for message of type 'ChangeFrequency-request"
  (cl:format cl:nil "uint32 frequency~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangeFrequency-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangeFrequency-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangeFrequency-request
    (cl:cons ':frequency (frequency msg))
))
;//! \htmlinclude ChangeFrequency-response.msg.html

(cl:defclass <ChangeFrequency-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ChangeFrequency-response (<ChangeFrequency-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangeFrequency-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangeFrequency-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name emotiv_epoc-srv:<ChangeFrequency-response> is deprecated: use emotiv_epoc-srv:ChangeFrequency-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangeFrequency-response>) ostream)
  "Serializes a message object of type '<ChangeFrequency-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangeFrequency-response>) istream)
  "Deserializes a message object of type '<ChangeFrequency-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangeFrequency-response>)))
  "Returns string type for a service object of type '<ChangeFrequency-response>"
  "emotiv_epoc/ChangeFrequencyResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeFrequency-response)))
  "Returns string type for a service object of type 'ChangeFrequency-response"
  "emotiv_epoc/ChangeFrequencyResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangeFrequency-response>)))
  "Returns md5sum for a message object of type '<ChangeFrequency-response>"
  "73ffa65309f649b8b694f03ce8799567")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangeFrequency-response)))
  "Returns md5sum for a message object of type 'ChangeFrequency-response"
  "73ffa65309f649b8b694f03ce8799567")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangeFrequency-response>)))
  "Returns full string definition for message of type '<ChangeFrequency-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangeFrequency-response)))
  "Returns full string definition for message of type 'ChangeFrequency-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangeFrequency-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangeFrequency-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangeFrequency-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ChangeFrequency)))
  'ChangeFrequency-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ChangeFrequency)))
  'ChangeFrequency-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeFrequency)))
  "Returns string type for a service object of type '<ChangeFrequency>"
  "emotiv_epoc/ChangeFrequency")