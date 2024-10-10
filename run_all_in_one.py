import os


def convert_xyz_to_ply(xyz_file, ply_file):
    with open(xyz_file, 'r') as xyz:
        points = xyz.readlines()

    # Prepare PLY file header and data
    ply_header = f"""ply
format ascii 1.0
element vertex {len(points)}
property float x
property float y
property float z
end_header
"""
    
    # Collect point data
    point_data = []
    for point in points:
        coords = point.strip().split()
        if len(coords) >= 3:  # Ensure there are at least x, y, z
            point_data.append(f"{coords[0]} {coords[1]} {coords[2]}")
    
    # Write to PLY file
    with open(ply_file, 'w') as ply:
        ply.write(ply_header)
        ply.write("\n".join(point_data) + "\n")

# Define the command to run

def run_isoconstraints(input_dir, output_dir):
    workdir = r'c:\Users\jianjun.x\Documents\projects\IsoConstraints'
    os.chdir(workdir)
    executable = r'.\Bin\x64\Release\PoissonRecon.exe'
    # ./data/think10k591234.xyz ./data/think10k591234.xyz ./results/think10k591234.ply false true true
    jet_exe = r'.\\jet\\normals_estimation.exe'
# ./jet/normals_estimation.exe input_xyz output_xyz neighbour_size 
    filenames = os.listdir(input_dir)
    for file in filenames:
        # if file != 'author1_car.xyz' : 
        #     continue
        input_file = os.path.join(input_dir, file) 
        print('input data file : ', input_file)
        estimate_n_file = os.path.join(output_dir, file) 
        normal_est_cmd  = f'{jet_exe} {input_file} {estimate_n_file} 10'
        exit_code = os.system(normal_est_cmd)
        print('normal file : ', estimate_n_file)
        filename = file.split('.')[0]
        output_file =  os.path.join(output_dir, filename + '.ply')
        print('output file : ', output_file)
        log_file = os.path.join(output_dir, filename + '_log.txt')
        print('log file : ', log_file)
        # Construct the command string
        command = f'{executable} {estimate_n_file} {estimate_n_file} {output_file} false false false > {log_file}'
        # Run the command
        exit_code = os.system(command)
        # Check the exit code
        if exit_code == 0:
            print("Execution was successful.")
        else:
            print(f"Execution failed with return code: {exit_code}")


def run_iPSR(input_dir, output_dir):
    workdir = r'C:\Users\jianjun.x\Documents\projects\ipsr'
    os.chdir(workdir)
    executable = r'.\Release\ipsr.exe'
    # ./data/think10k591234.xyz ./data/think10k591234.xyz ./results/think10k591234.ply false true true
    # ./jet/normals_estimation.exe input_xyz output_xyz neighbour_size 
    print(input_dir)
    filenames = os.listdir(input_dir)
    for file in filenames:
        # print(file)
        # if file != 'author1_car.xyz' : 
        #     continue
        input_file = os.path.join(input_dir, file) 
        filename = file.split('.')[0]
        plyfile = os.path.join(output_dir, filename + '_pt.ply')
        convert_xyz_to_ply(input_file, plyfile)

        output_file =  os.path.join(output_dir, filename + '.ply')
        print('output file : ', output_file)
        log_file = os.path.join(output_dir, filename + '_log.txt')
        print('log file : ', log_file)
        # Construct the command string
        command = f'{executable} --in {plyfile} --out  {output_file} > {log_file}'
        # Run the command
        exit_code = os.system(command)
        # Check the exit code
        if exit_code == 0:
            print("Execution was successful.")
        else:
            print(f"Execution failed with return code: {exit_code}")

def run_gcno(input_dir, output_dir):
    
    executable = r'c:\Users\jianjun.x\Documents\projects\GCNO\build\MAIN\Release\MAIN.exe'
    # ./data/think10k591234.xyz ./data/think10k591234.xyz ./results/think10k591234.ply false true true
    # ./jet/normals_estimation.exe input_xyz output_xyz neighbour_size 
    workdir = r'c:\Users\jianjun.x\Documents\projects\IsoConstraints'
    os.chdir(workdir)
    jet_exe = r'.\\jet\\normals_estimation.exe'

    filenames = os.listdir(input_dir)
    for file in filenames:
        input_file = os.path.join(input_dir, file) 

        estimate_n_file = os.path.join(output_dir, file) 
        normal_est_cmd  = f'{jet_exe} {input_file} {estimate_n_file} 10'
        exit_code = os.system(normal_est_cmd)

        filename = file.split('.')[0]
        log_file = os.path.join(output_dir, filename + '_log.txt')
        print('log file : ', log_file)
        # Construct the command string
        command = f'{executable} --indir {output_dir} --name {filename} --outdir  {output_dir} > {log_file}'
        # Run the command
        exit_code = os.system(command)
        # Check the exit code
        if exit_code == 0:
            print("Execution was successful.")
        else:
            print(f"Execution failed with return code: {exit_code}")

def run_vipss(input_dir, output_dir):
    workdir = r'C:\Users\jianjun.x\Documents\projects\VIPSS'
    os.chdir(workdir)
    executable = r'.\x64\Release\VIPSS.exe'
    filenames = os.listdir(input_dir)
    for file in filenames:
        input_file = os.path.join(input_dir, file) 
        print('input file : ', input_file)
        filename = file.split('.')[0]
        if filename == 'chair36' or filename == 'chinese_bowl'  or filename == 'flower_pot' :
            continue
        output_file = os.path.join(output_dir, filename) 
        print('output file : ', os.path.join(output_dir, filename) )
        log_file = os.path.join(output_dir, filename + '.txt')
        print('log file : ', log_file)
        # Construct the command string
        if filename == 'walrus' or filename == 'cassie_vacuum' or filename == 'author1_car':
            command = f'{executable} -infile {input_file} -outpath {output_file} -lambda 0.001 > {log_file}'
        else :
            command = f'{executable} -infile {input_file} -outpath {output_file} > {log_file}'
        # Run the command
        exit_code = os.system(command)

        # Check the exit code
        if exit_code == 0:
            print("Execution was successful.")
        else:
            print(f"Execution failed with return code: {exit_code}")

def run_localvipss(input_dir, output_dir):
    workdir = r'C:\Users\jianjun.x\Documents\projects\VIPSS_LOCAL'

    os.chdir(workdir)
    executable = r'.\bin\LocalVipss.exe'
    possion_exe = r'c:\Users\jianjun.x\Documents\projects\AdaptiveSolvers.x64\PoissonRecon.exe'

    filenames = os.listdir(input_dir)
    for file in filenames:
        
        # if file != 'author1_car.xyz' : 
        #     continue
        input_file = os.path.join(input_dir, file) 
        print('input file : ', input_file)
       
        filename = file.split('.')[0]
        # if filename != 'flowrep_spherecylinder':
        #     continue
        
        output_file = os.path.join(output_dir, filename + '.ply') 
        print('output file : ', output_file)
        log_file = os.path.join(output_dir, filename + '.txt')
        print('log file : ', log_file)
        # Construct the command string
        command = f'{executable} -input {input_file} -output {output_file} > {log_file}'
        if filename == 'cassie_vacuum'   :
            command = f'{executable} -input {input_file} -output {output_file} -lambda 0.001 > {log_file}'
        if  filename == 'author1_car'  :
            command = f'{executable} -input {input_file} -output {output_file} -lambda 0.001  > {log_file}'

        if filename == 'ils_car2.ply' or filename == 'torus_wires':
            command = f'{executable} -input {input_file} -output {output_file} -initPV 0 > {log_file}'
        
        # print(command)
        # Run the command
        exit_code = os.system(command)

        log_file = os.path.join(output_dir, filename + '_possion.txt')
        pt_file = os.path.join(output_dir, filename + '_out_normal.ply') 
        output_file = os.path.join(output_dir, filename + '_possion_mesh.ply')
        command = f'{possion_exe} --in {pt_file} --out {output_file} --depth 10 > {log_file}'
        exit_code = os.system(command)
        # Check the exit code
        if exit_code == 0:
            print("Execution was successful.")
        else:
            print(f"Execution failed with return code: {exit_code}")

            
def run_PGR(input_dir, output_dir):
    workdir = r'/home/jianjun/Documents/projects/ParametricGaussRecon'
    os.chdir(workdir)
    executable = r'python run_pgr.py '
    # ./data/think10k591234.xyz ./data/think10k591234.xyz ./results/think10k591234.ply false true true
    # ./jet/normals_estimation.exe input_xyz output_xyz neighbour_size 
    filenames = os.listdir(input_dir)
    for file in filenames:
        input_file = os.path.join(input_dir, file) 
        filename = filename = file.split('.')[0]
        log_file = os.path.join(output_dir, filename + '_log.txt')
        print('log file : ', log_file)
        # Construct the command string
        command = f'{executable} {input_file} --alpha 2 -wmin 0.04 --outdir {output_dir} > {log_file}'
        # Run the command
        exit_code = os.system(command)
        # Check the exit code
        if exit_code == 0:
            print("Execution was successful.")
        else:
            print(f"Execution failed with return code: {exit_code}")

def run_WNNC(input_dir, output_dir):
    workdir = r'/home/jianjun/Documents/projects/WNNC'
    os.chdir(workdir)
    executable = r'./main_GaussReconCUDA '
    
    normalExe = r'python main_wnnc.py '
    # ./data/think10k591234.xyz ./data/think10k591234.xyz ./results/think10k591234.ply false true true
    # ./jet/normals_estimation.exe input_xyz output_xyz neighbour_size 
    filenames = os.listdir(input_dir)
    for file in filenames:
        input_file = os.path.join(input_dir, file) 
        filename = filename = file.split('.')[0]
        log_file = os.path.join(output_dir, filename + '_log.txt')
        print('log file : ', log_file)
        outfile = os.path.join(output_dir, filename + '.ply') 
        # Construct the command string
        command = f'{executable} -i {input_file} -o {outfile} -w 0.05 > {log_file}'
        # Run the command
        exit_code = os.system(command)
        log_file = os.path.join(output_dir, filename + '_log_normal.txt')
        command = f'{normalExe}  {input_file} --out_dir {output_dir} --width_config l5 --tqdm > {log_file}'
        exit_code = os.system(command)
        
        # Check the exit code
        if exit_code == 0:
            print("Execution was successful.")
        else:
            print(f"Execution failed with return code: {exit_code}")



data_list = ['vipss_data','sketches',"sparse"]
method_list = ['ipsr', 'isoconstraints', 'gcno', 'localvipss', 'vipss', "PGR"]

data_folder = 'sparse'
method = 'vipss'

input_dir = r'C:\Users\jianjun.x\Documents\projects\3D_pointcloud_dataset\contours' 
input_dir = os.path.join(input_dir, data_folder)
output_dir = r'c:\Users\jianjun.x\Documents\projects\3D_pointcloud_dataset\results'
output_dir = os.path.join(output_dir, method)
if not os.path.exists(output_dir) :
        os.mkdir(output_dir)

output_dir = os.path.join(output_dir, data_folder)
if not os.path.exists(output_dir) :
        os.mkdir(output_dir)

items = os.listdir(input_dir)

for folder in items:
    cur_in_dir = os.path.join(input_dir, folder)
    cur_out_dir = os.path.join(output_dir, folder)
    if not os.path.exists(cur_out_dir) :
        os.mkdir(cur_out_dir)

    if method == "gcno":
        run_gcno(cur_in_dir, cur_out_dir)
    if method == "ipsr":
        run_iPSR(cur_in_dir, cur_out_dir)
    if method == "isoconstraints":
        run_isoconstraints(cur_in_dir, cur_out_dir)
    if method == "vipss":
        run_vipss(cur_in_dir, cur_out_dir)
    if method == "PGR":
        run_PGR(cur_in_dir, cur_out_dir)
    if method == "WNNC":
        run_WNNC(cur_in_dir, cur_out_dir)
    if method == "localvipss":
        run_localvipss(cur_in_dir, cur_out_dir)


# run_isoconstraints(input_dir, output_dir)
