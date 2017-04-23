
(cl:in-package :asdf)

(defsystem "emotiv_epoc-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "EEGFrame" :depends-on ("_package_EEGFrame"))
    (:file "_package_EEGFrame" :depends-on ("_package"))
  ))