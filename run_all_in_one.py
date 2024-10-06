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
    filenames = os.listdir(input_dir)
    for file in filenames:
        
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
    filenames = os.listdir(input_dir)
    for file in filenames:
        # input_file = os.path.join(input_dir, file) 
        filename = file.split('.')[0]
        log_file = os.path.join(output_dir, filename + '_log.txt')
        print('log file : ', log_file)
        # Construct the command string
        command = f'{executable} --indir {input_dir} --name {filename} --outdir  {output_dir} > {log_file}'
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
        output_file = os.path.join(output_dir, filename) 
        print('output file : ', os.path.join(output_dir, filename) )
        log_file = os.path.join(output_dir, filename + '.txt')
        print('log file : ', log_file)
        # Construct the command string
        if filename == 'walrus':
            command = f'{executable} -infile {input_file} -outpath {output_file} -lambda 0.003 > {log_file}'
        else :
            command = f'{executable} -infile {input_file} -outpath {output_file} > {log_file}'
        # Run the command
        exit_code = os.system(command)

        # Check the exit code
        if exit_code == 0:
            print("Execution was successful.")
        else:
            print(f"Execution failed with return code: {exit_code}")

data_list = ['vipss_data']
method_list = ['iprs', 'isoconstraints', 'gcno', 'local_vipss', 'vipss']

data_folder = 'vipss_data'
method = 'vipss'

input_dir = r'C:\Users\jianjun.x\Documents\projects\3D_pointcloud_dataset\contours' 
input_dir = os.path.join(input_dir, data_folder)
output_dir = r'c:\Users\jianjun.x\Documents\projects\3D_pointcloud_dataset\results'
output_dir = os.path.join(output_dir, method, data_folder)

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


# run_isoconstraints(input_dir, output_dir)
