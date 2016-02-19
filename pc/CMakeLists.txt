# This is dirty hack. This will enable to build gmock on ubuntu desktop without building package.
IF (NOT DEFINED INCLUDE_INSTALL_DIR)
    SET(INCLUDE_INSTALL_DIR ${CMAKE_INSTALL_PREFIX}/include)
ENDIF (NOT DEFINED INCLUDE_INSTALL_DIR)

IF (NOT DEFINED LIB_INSTALL_DIR)
    SET(LIB_INSTALL_DIR ${CMAKE_INSTALL_PREFIX}/lib)
ENDIF (NOT DEFINED LIB_INSTALL_DIR)

IF (NOT DEFINED PKG_VERSION)
    SET(PKG_VERSION "1.7.0-update1")
ENDIF (NOT DEFINED PKG_VERSION)

configure_file(gmock.pc.in gmock.pc @ONLY)
configure_file(gmock_main.pc.in gmock_main.pc @ONLY)
install(FILES gmock.pc gmock_main.pc DESTINATION lib/pkgconfig)
