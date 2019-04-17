
from cpp2py.wrap_generator import *

# The module
module = module_(full_name = "lattice", doc = "Green's function lattice tools", app_name = "lattice")

# All the triqs C++/Python modules
import pytriqs.gf
import pytriqs.lattice

# Add here all includes beyond what is automatically included by the triqs modules
module.add_include("triqs_tprf/types.hpp") # Manually added
module.add_include("triqs_tprf/lattice.hpp") # Manually added

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
#include <triqs/lattice/brillouin_zone.hpp>

#include <cpp2py/converters/map.hpp>
#include <cpp2py/converters/optional.hpp>
#include <cpp2py/converters/pair.hpp>
#include <cpp2py/converters/set.hpp>
#include <cpp2py/converters/string.hpp>
#include <cpp2py/converters/vector.hpp>
#include <triqs/cpp2py_converters/arrays.hpp>
#include <triqs/cpp2py_converters/gf.hpp>
#include <cpp2py/converters/variant.hpp>

using namespace triqs::gfs;
using namespace triqs::lattice;
using namespace triqs_tprf;
""")

module.add_function("array<std::complex<double>, 6> cluster_mesh_fourier_interpolation(array<double, 2> k_vecs, chi_wr_cvt chi)", doc = """""")

# -- Dyson

module.add_function("g_wk_t lattice_dyson_g0_wk(double mu, e_k_cvt e_k, gf_mesh<imfreq> mesh)", doc = """""")
module.add_function("gk_iw_t lattice_dyson_g_wk(double mu, e_k_cvt e_k, g_w_cvt sigma_w)", doc = """""")
module.add_function("g_wk_t lattice_dyson_g_wk(double mu, e_k_cvt e_k, g_wk_cvt sigma_wk)", doc = """""")
module.add_function("g_w_t lattice_dyson_g_w(double mu, e_k_cvt e_k, g_w_cvt sigma_w)", doc = """""")


module.add_function("g_wr_t fourier_wk_to_wr(g_wk_cvt g_wk)", doc = """""")
module.add_function("g_wk_t fourier_wr_to_wk(g_wr_cvt g_wr)", doc = """""")
module.add_function("g_tr_t fourier_wr_to_tr(g_wr_cvt g_wr, int ntau=-1)", doc = """""")

# -- Bubble in imaginary time

module.add_function("chi_tr_t chi0_tr_from_grt_PH(gr_tau_vt grt)", doc = """""")
module.add_function("chi_wr_t chi0_w0r_from_grt_PH(gr_tau_vt grt)", doc = """""")
module.add_function("chi_wr_t chi_w0r_from_chi_tr(chi_tr_vt chi_tr)", doc = """""")
module.add_function("chi_wr_t chi_wr_from_chi_tr(chi_tr_vt chi_tr, int nw)", doc = """""")
module.add_function("chi_wk_t chi_wk_from_chi_wr(chi_wr_vt chi_wr)", doc = """""")
module.add_function("chi_wr_t chi_wr_from_chi_wk(chi_wk_vt chi_wk)", doc = """""")

# -- Bubble static analytic

module.add_function("chi_wk_t lindhard_chi00_wk(gf<brillouin_zone, matrix_valued> e_k, int nw, double beta, double mu)", doc = """""")

# -- RPA

module.add_function("chi_wk_t solve_rpa_PH(chi_wk_vt chi0, array_view<std::complex<double>, 4> U)", doc = """""")

# -- GW

module.add_function("chi_wk_t screened_interaction_W(chi_wk_vt PI_wk, chi_k_vt V_k)", doc = """""")
module.add_function("g_wk_t gw_self_energy(chi_wk_vt W_wk, g_wk_vt g_wk)", doc = """""")

# -- Eliashberg

module.add_function("gk_iw_t eliashberg_product(chi_wk_vt Gamma_pp, gk_iw_vt g_wk, gk_iw_vt delta_wk)", doc = """""")
module.add_function("gk_iw_t eliashberg_product_fft(chi_tr_vt Gamma_pp_dyn_tr, chi_r_vt Gamma_pp_const_r, gk_iw_vt g_wk, gk_iw_vt delta_wk)", doc = """""")
module.add_function("gk_iw_t eliashberg_g_delta_g_product(gk_iw_vt g_wk, gk_iw_vt delta_wk)", doc = """""")
module.add_function("std::tuple<chi_wk_vt, chi_k_vt> split_into_dynamic_wk_and_constant_k(chi_wk_vt Gamma_pp)", doc = """""")
module.add_function("std::tuple<chi_tr_vt, chi_r_vt> dynamic_and_constant_to_tr(chi_wk_vt Gamma_pp_dyn_wk, chi_k_vt Gamma_pp_const_k)", doc = """""")
module.add_function("chi_wk_t gamma_PP_singlet(chi_wk_vt chi_c, chi_wk_vt chi_s, array_view<std::complex<double>, 4> U_c, array_view<std::complex<double>, 4> U_s)", doc = """""")

# -- Full BSE functions

module.add_function("chi0r_t chi0r_from_gr_PH(int nw, int nnu, gf_view<cartesian_product<imfreq, cyclic_lattice>> gr)", doc = """""")
module.add_function("chi0r_t chi0r_from_gr_PH_nompi(int nw, int nnu, gf_view<cartesian_product<imfreq, cyclic_lattice>> gr)", doc = """""")
module.add_function("chi0q_t chi0q_from_g_wk_PH(int nw, int nnu, gf_view<cartesian_product<imfreq, brillouin_zone>> g_wk)", doc = """""")

module.add_function("chi0r_t chi0r_from_chi0q(gf_view<cartesian_product<imfreq, imfreq, brillouin_zone>, tensor_valued<4>> chi0q)", doc = """""")
module.add_function("chi0q_t chi0q_from_chi0r(gf_view<cartesian_product<imfreq, imfreq, cyclic_lattice>, tensor_valued<4>> chi0r)", doc = """""")

module.add_function ("gf<cartesian_product<imfreq, brillouin_zone>, tensor_valued<4>> chi0q_sum_nu(gf_view<cartesian_product<imfreq, imfreq, brillouin_zone>, tensor_valued<4>> chi0q)", doc = """""")
module.add_function ("gf<cartesian_product<imfreq, brillouin_zone>, tensor_valued<4>> chi0q_sum_nu_tail_corr_PH(gf_view<cartesian_product<imfreq, imfreq, brillouin_zone>, tensor_valued<4>> chi0q)", doc = """""")

module.add_function ("gf<imfreq, tensor_valued<4>> chi0q_sum_nu_q(chi0q_t chi0q)", doc = """""")

module.add_function("chiq_t chiq_from_chi0q_and_gamma_PH(gf_view<cartesian_product<imfreq, imfreq, brillouin_zone>, tensor_valued<4>> chi0q, gf_view<cartesian_product<imfreq, imfreq, imfreq>, tensor_valued<4>> gamma_ph)", doc = """""")

module.add_function("gf<cartesian_product<brillouin_zone, imfreq>, tensor_valued<4>> chiq_sum_nu_from_chi0q_and_gamma_PH(gf_view<cartesian_product<imfreq, imfreq, brillouin_zone>, tensor_valued<4>> chi0q, gf_view<cartesian_product<imfreq, imfreq, imfreq>, tensor_valued<4>> gamma_ph)", doc = """""")

module.add_function("gf<cartesian_product<brillouin_zone, imfreq>, tensor_valued<4>> chiq_sum_nu_from_g_wk_and_gamma_PH(gk_iw_t g_wk, g2_iw_vt gamma_ph_wnn, int tail_corr_nwf=-1)", doc = """""")

module.add_function("gf<cartesian_product<brillouin_zone, imfreq>, tensor_valued<4>> chiq_sum_nu_from_e_k_sigma_w_and_gamma_PH(double mu, ek_vt e_k, g_iw_vt sigma_w, g2_iw_vt gamma_ph_wnn, int tail_corr_nwf=-1)", doc = """""")

module.add_function ("gf<cartesian_product<brillouin_zone, imfreq>, tensor_valued<4>> chiq_sum_nu(gf_view<cartesian_product<brillouin_zone, imfreq, imfreq, imfreq>, tensor_valued<4>> chiq)", doc = """""")

module.add_function ("gf<imfreq, tensor_valued<4>> chiq_sum_nu_q(gf_view<cartesian_product<brillouin_zone, imfreq, imfreq, imfreq>, tensor_valued<4>> chiq)", doc = """""")

module.generate_code()