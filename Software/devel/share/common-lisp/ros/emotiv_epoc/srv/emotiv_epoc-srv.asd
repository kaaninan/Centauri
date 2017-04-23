
(cl:in-package :asdf)

(defsystem "emotiv_epoc-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ChangeFrequency" :depends-on ("_package_ChangeFrequency"))
    (:file "_package_ChangeFrequency" :depends-on ("_package"))
  ))