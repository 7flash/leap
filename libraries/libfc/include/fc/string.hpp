#pragma once
#include <cstdint>
#include <limits>
#include <string>

namespace fc
{
  int64_t  to_int64( const std::string& );
  uint64_t to_uint64( const std::string& );
  double   to_double( const std::string& );
  std::string to_string( double );
  std::string to_string( uint64_t );
  std::string to_string( int64_t );
  std::string to_string( uint16_t );
  inline std::string to_string( int32_t v ) { return to_string( int64_t(v) ); }
  inline std::string to_string( uint32_t v ){ return to_string( uint64_t(v) ); }
#ifdef __APPLE__
  inline std::string to_string( size_t s) { return to_string(uint64_t(s)); }
#endif

  class variant_object;
  std::string format_string( const std::string&, const variant_object&, bool minimize = false );
  std::string trim( const std::string& );

  /**
   * Convert '\t', '\r', '\n', '\\' and '"'  to "\t\r\n\\\"" if escape_ctrl == on
   * Convert all other < 32 & 127 ascii to escaped unicode "\u00xx"
   * Removes invalid utf8 characters
   * Escapes Control sequence Introducer 0x9b to \u009b
   * All other characters unmolested.
   *
   * @param str input/output string to escape/truncate
   * @param escape_ctrl if on escapes control chars in str
   * @param max_len truncate string to max_len
   * @param add_truncate_str if truncated by max_len, add add_truncate_str to end of any truncated string,
   *                         new length with be max_len + add_truncate_str.size()
   * @return pair<reference to possibly modified passed in str, true if modified>
   */
  enum class escape_control_chars { off, on };
  std::pair<std::string&, bool> escape_str( std::string& str, escape_control_chars escape_ctrl = escape_control_chars::on,
                                            std::size_t max_len = std::numeric_limits<std::size_t>::max(),
                                            std::string_view add_truncate_str = "..." );
}
